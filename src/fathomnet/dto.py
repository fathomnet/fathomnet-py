# dto.py (fathomnet-py)
import os
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, Generic, List, Optional, TypeVar

from pydantic import BaseModel, TypeAdapter, field_validator
from lxml import etree
from lxml.builder import E
from requests.auth import AuthBase

_DATETIME_ADAPTER = TypeAdapter(datetime)

T = TypeVar("T")


def _to_rfc3339(value: Optional[str]) -> Optional[str]:
    """Parse any RFC 3339 / ISO 8601 datetime (or bare date) string and
    reformat it to the RFC 3339 shape the FathomNet API requires,
    e.g. "2007-08-02T00:00:00.000Z"."""
    if value is None:
        return None
    dt = _DATETIME_ADAPTER.validate_python(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    dt = dt.astimezone(timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%S.") + f"{dt.microsecond // 1000:03d}Z"


class DTO(BaseModel):
    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "DTO":
        return cls(**d)

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()


class AImageDTO(DTO):
    id: Optional[int] = None
    uuid: Optional[str] = None
    url: Optional[str] = None
    valid: Optional[bool] = None
    imagingType: Optional[str] = None
    depthMeters: Optional[float] = None
    height: Optional[int] = None
    lastValidation: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    salinity: Optional[float] = None
    temperatureCelsius: Optional[float] = None
    oxygenMlL: Optional[float] = None
    pressureDbar: Optional[float] = None
    mediaType: Optional[str] = None
    modified: Optional[str] = None
    sha256: Optional[str] = None
    contributorsEmail: Optional[str] = None
    tags: Optional[List["ATagDTO"]] = None
    timestamp: Optional[str] = None
    width: Optional[int] = None
    boundingBoxes: Optional[List["ABoundingBoxDTO"]] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None
    imageLicense: Optional[str] = None

    def to_pascal_voc(
        self, path: Optional[str] = None, pretty_print: bool = False
    ) -> str:
        """Convert to a Pascal VOC.

        :param path: Path to the image file, defaults to using the image URL if available
        :type path: Optional[str], optional
        :param pretty_print: Set true to add indentation and newlines in XML, defaults to False
        :type pretty_print: bool, optional
        :raises ValueError: Raised if both the path and image URL are unspecified
        :return: Pascal VOC encoded string
        :rtype: str
        """
        if path is None:  # If no path provided, use URL
            if self.url is None:
                raise ValueError(
                    "Either the path argument or the image URL must be specified."
                )
            path = self.url

        # Parse the folder name and file name
        dir_path, base_name = os.path.split(path)
        folder_name = os.path.basename(dir_path)

        # Encode bounding box data into object tags
        boxes = self.boundingBoxes or []
        objects = [
            E.object(
                E.name(
                    box.concept
                    + (
                        " {}".format(box.altConcept)
                        if box.altConcept is not None
                        else ""
                    )
                ),
                E.pose("Unspecified"),
                E.truncated(
                    str(int(box.truncated) if box.truncated is not None else 0)
                ),
                E.difficult("0"),
                E.occluded(str(int(box.occluded) if box.occluded is not None else 0)),
                E.bndbox(
                    E.xmin(str(1 + box.x)),
                    E.xmax(str(1 + box.x + box.width)),
                    E.ymin(str(1 + box.y)),
                    E.ymax(str(1 + box.y + box.height)),
                ),
            )
            for box in boxes
        ]

        # Encode annotation data
        annotation = E.annotation(
            E.folder(folder_name),
            E.filename(base_name),
            E.path(path),
            E.source(E.database("FathomNet")),
            E.size(E.width(str(self.width)), E.height(str(self.height)), E.depth("3")),
            E.segmented("0"),
            *objects,
        )

        return etree.tostring(annotation, pretty_print=pretty_print).decode()


class ATagDTO(DTO):
    id: Optional[int] = None
    uuid: Optional[str] = None
    key: Optional[str] = None
    mediaType: Optional[str] = None
    value: Optional[str] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None
    image: Optional[AImageDTO] = None


class TagDTO(ATagDTO):
    imageUuid: Optional[str] = None


class ReviewState(str, Enum):
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"


class ABoundingBoxDTO(DTO):
    id: Optional[int] = None
    uuid: Optional[str] = None
    userDefinedKey: Optional[str] = None
    concept: Optional[str] = None
    altConcept: Optional[str] = None
    image: Optional[AImageDTO] = None
    groupOf: Optional[bool] = None
    height: Optional[int] = None
    occluded: Optional[bool] = None
    observer: Optional[str] = None
    truncated: Optional[bool] = None
    width: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
    rejected: Optional[bool] = None
    reviewState: Optional[ReviewState] = None
    reviewer: Optional[str] = None
    lastReviewedTimestamp: Optional[str] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None
    annotationLicense: Optional[str] = None


class ApiKey(DTO):
    uuid: Optional[str] = None
    apiKey: Optional[str] = None


class AuthHeader(DTO, AuthBase):
    type: Optional[str] = None
    token: Optional[str] = None

    @property
    def auth_dict(self):
        return {"Authorization": "{} {}".format(self.type, self.token)}

    def __call__(self, r):
        r.headers.update(self.auth_dict)
        return r


class Authentication(DTO):
    attributes: Optional[object] = None


class ParsedJwt(DTO):
    email: Optional[str] = None
    displayName: Optional[str] = None
    groups: Optional[List[str]] = None
    expiresAt: Optional[str] = None


class BoundingBoxDTO(ABoundingBoxDTO):
    imageUuid: Optional[str] = None


class BoundingBox(DTO):
    uuid: Optional[str] = None
    id: Optional[int] = None
    userDefinedKey: Optional[str] = None
    concept: Optional[str] = None
    altConcept: Optional[str] = None
    image: Optional["Image"] = None
    groupOf: Optional[bool] = None
    height: Optional[int] = None
    occluded: Optional[bool] = None
    observer: Optional[str] = None
    truncated: Optional[bool] = None
    width: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None
    reviewState: Optional[ReviewState] = None
    reviewer: Optional[str] = None
    lastReviewedTimestamp: Optional[str] = None
    annotationLicense: Optional[str] = None


class BoundingBoxSort(DTO):
    class Field(str, Enum):
        CREATED = "CREATED"
        CREATED_AT = "CREATED"  # Deprecated alias of CREATED
        UUID = "UUID"
        CONCEPT = "CONCEPT"
        UPDATED = "UPDATED"
        REVIEWED = "REVIEWED"
        IMAGE_URL = "IMAGE_URL"
        ROI_SIZE = "ROI_SIZE"

    class Direction(str, Enum):
        ASC = "ASC"
        DESC = "DESC"

    field: Optional[Field] = None
    direction: Optional[Direction] = None


class BoundingBoxConstraintsDTO(DTO):
    concept: Optional[str] = None
    taxaProviderName: Optional[str] = None
    contributorsEmails: Optional[List[str]] = None
    startTimestamp: Optional[str] = None
    endTimestamp: Optional[str] = None
    includeUnverified: Optional[bool] = None
    includeVerified: Optional[bool] = None
    includeRejected: Optional[bool] = None
    includeUnknown: Optional[bool] = None
    minLongitude: Optional[float] = None
    maxLongitude: Optional[float] = None
    minLatitude: Optional[float] = None
    maxLatitude: Optional[float] = None
    minDepth: Optional[float] = None
    maxDepth: Optional[float] = None
    ownerInstitutionCodes: Optional[List[str]] = None
    collectionCodes: Optional[List[str]] = None
    tagKeys: Optional[List[str]] = None
    imagingTypes: Optional[List[str]] = None
    imageLicenses: Optional[List[str]] = None
    annotationLicenses: Optional[List[str]] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    sort: Optional[BoundingBoxSort] = None

    @field_validator("startTimestamp", "endTimestamp")
    @classmethod
    def _format_timestamp(cls, value: Optional[str]) -> Optional[str]:
        return _to_rfc3339(value)


class ByConceptCount(DTO):
    concept: Optional[str] = None
    count: Optional[int] = None


class ByObserverCount(DTO):
    observer: Optional[str] = None
    count: Optional[int] = None


class ByReviewerCount(DTO):
    reviewer: Optional[str] = None
    count: Optional[int] = None


class ByContributorCount(DTO):
    contributorsEmail: Optional[str] = None
    count: Optional[int] = None


class BDarwinCore(DTO):
    uuid: Optional[str] = None
    recordType: Optional[str] = None
    basisOfRecord: Optional[str] = None
    datasetID: Optional[str] = None
    recordLanguage: Optional[str] = None
    license: Optional[str] = None
    modified: Optional[str] = None
    ownerInstitutionCode: Optional[str] = None
    accessRights: Optional[str] = None
    bibliographicCitation: Optional[str] = None
    collectionCode: Optional[str] = None
    collectionID: Optional[str] = None
    dataGeneralizations: Optional[str] = None
    datasetName: Optional[str] = None
    dynamicProperties: Optional[str] = None
    informationWithheld: Optional[str] = None
    institutionCode: Optional[str] = None
    institutionID: Optional[str] = None
    recordReferences: Optional[str] = None
    rightsHolder: Optional[str] = None


class BImageSetUploadDTO(DTO):
    uuid: Optional[str] = None
    localPath: Optional[str] = None
    remoteUri: Optional[str] = None
    sha256: Optional[str] = None
    format: Optional["ImageSetUpload.UploadFormat"] = None
    contributorsEmail: Optional[str] = None
    status: Optional["ImageSetUpload.Status"] = None
    statusUpdaterEmail: Optional[str] = None
    statusUpdateTimestamp: Optional[str] = None
    contributorNotificationTimestamp: Optional[str] = None
    rejectionReason: Optional[str] = None
    rejectionDetails: Optional[str] = None
    darwinCore: Optional[BDarwinCore] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


class Count(DTO):
    objectType: Optional[str] = None
    count: Optional[int] = None


class DarwinCore(DTO):
    id: Optional[int] = None
    uuid: Optional[str] = None
    recordType: Optional[str] = None
    basisOfRecord: Optional[str] = None
    datasetID: Optional[str] = None
    recordLanguage: Optional[str] = None
    license: Optional[str] = None
    modified: Optional[str] = None
    ownerInstitutionCode: Optional[str] = None
    accessRights: Optional[str] = None
    bibliographicCitation: Optional[str] = None
    collectionCode: Optional[str] = None
    collectionID: Optional[str] = None
    dataGeneralizations: Optional[str] = None
    datasetName: Optional[str] = None
    dynamicProperties: Optional[str] = None
    informationWithheld: Optional[str] = None
    institutionCode: Optional[str] = None
    institutionID: Optional[str] = None
    recordReferences: Optional[str] = None
    rightsHolder: Optional[str] = None
    imageSetUpload: Optional["ImageSetUpload"] = None


class FathomnetIdAdminMutation(DTO):
    disabled: Optional[bool] = None
    expertiseRank: Optional[str] = None
    roleData: Optional[str] = None
    organization: Optional[str] = None


class FathomnetIdMutation(DTO):
    jobTitle: Optional[str] = None
    organization: Optional[str] = None
    profile: Optional[str] = None
    displayName: Optional[str] = None
    orcid: Optional[str] = None
    notificationFrequency: Optional[str] = None


class FathomnetIdentity(DTO):
    id: Optional[int] = None
    uuid: Optional[str] = None
    email: Optional[str] = None
    firebaseUid: Optional[str] = None
    roleData: Optional[str] = None
    organization: Optional[str] = None
    jobTitle: Optional[str] = None
    profile: Optional[str] = None
    apiKey: Optional[str] = None
    avatarUrl: Optional[str] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None
    disabled: Optional[bool] = None
    expertiseRank: Optional[str] = None
    displayName: Optional[str] = None
    roles: Optional[List["Roles"]] = None
    orcid: Optional[str] = None
    notificationFrequency: Optional[str] = None


class GeoImage(DTO):
    uuid: Optional[str] = None
    url: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    depthMeters: Optional[float] = None
    contributorsEmail: Optional[str] = None
    timestamp: Optional[str] = None
    valid: Optional[bool] = None
    lastValidation: Optional[str] = None
    imageLicense: Optional[str] = None


class GeoImageConstraints(DTO):
    concept: Optional[str] = None
    taxaProviderName: Optional[str] = None
    contributorsEmail: Optional[str] = None
    startTimestamp: Optional[str] = None
    endTimestamp: Optional[str] = None
    imagingTypes: Optional[List[str]] = None
    imageLicenses: Optional[List[str]] = None
    includeUnverified: Optional[bool] = None
    includeVerified: Optional[bool] = None
    minLongitude: Optional[float] = None
    maxLongitude: Optional[float] = None
    minLatitude: Optional[float] = None
    maxLatitude: Optional[float] = None
    minDepth: Optional[float] = None
    maxDepth: Optional[float] = None
    ownerInstitutionCodes: Optional[List[str]] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    newestFirst: Optional[bool] = None

    @field_validator("startTimestamp", "endTimestamp")
    @classmethod
    def _format_timestamp(cls, value: Optional[str]) -> Optional[str]:
        return _to_rfc3339(value)


class GeoImageConstraintsCount(DTO):
    constraints: Optional[GeoImageConstraints] = None
    count: Optional[int] = None


class Image(DTO):
    id: Optional[int] = None
    uuid: Optional[str] = None
    url: Optional[str] = None
    valid: Optional[bool] = None
    imagingType: Optional[str] = None
    depthMeters: Optional[float] = None
    height: Optional[int] = None
    lastValidation: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    salinity: Optional[float] = None
    temperatureCelsius: Optional[float] = None
    oxygenMlL: Optional[float] = None
    pressureDbar: Optional[float] = None
    mediaType: Optional[str] = None
    modified: Optional[str] = None
    sha256: Optional[str] = None
    contributorsEmail: Optional[str] = None
    timestamp: Optional[str] = None
    width: Optional[int] = None
    tags: Optional[List["Tag"]] = None
    boundingBoxes: Optional[List[BoundingBox]] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None
    imageSetUploads: Optional[List["ImageSetUpload"]] = None
    imageLicense: Optional[str] = None


class ImageSetUpload(DTO):
    class Status(Enum):
        PENDING = "PENDING"
        ACCEPTED = "ACCEPTED"
        REJECTED = "REJECTED"

    class UploadFormat(Enum):
        CSV = "CSV"
        UNSUPPORTED = "UNSUPPORTED"

    id: Optional[int] = None
    uuid: Optional[str] = None
    localPath: Optional[str] = None
    remoteUri: Optional[str] = None
    sha256: Optional[str] = None
    contributorsEmail: Optional[str] = None
    status: Optional[Status] = None
    rejectionReason: Optional[str] = None
    rejectionDetails: Optional[str] = None
    statusUpdaterEmail: Optional[str] = None
    statusUpdateTimestamp: Optional[str] = None
    contributorNotificationTimestamp: Optional[str] = None
    format: Optional[UploadFormat] = None
    darwinCore: Optional[DarwinCore] = None
    images: Optional[List[Image]] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


class ImageSetUploadStats(DTO):
    imageSetUploadUuid: Optional[str] = None
    imageCount: Optional[int] = None
    boundingBoxCount: Optional[int] = None
    verifiedBoundingBoxCount: Optional[int] = None


class MarineRegion(DTO):
    id: Optional[int] = None
    MRGID: Optional[int] = None
    name: Optional[str] = None
    minLatitude: Optional[float] = None
    maxLatitude: Optional[float] = None
    minLongitude: Optional[float] = None
    maxLongitude: Optional[float] = None
    centerLatitude: Optional[float] = None
    centerLongitude: Optional[float] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


class Message(DTO):
    message: Optional[str] = None


class Sort(DTO):
    class Order(DTO):
        class Direction(Enum):
            ASC = "ASC"
            DESC = "DESC"

        ignoreCase: Optional[bool] = None
        direction: Optional[Direction] = None
        property: Optional[str] = None
        ascending: Optional[bool] = None

    sorted: Optional[bool] = None
    orderBy: Optional[List[Order]] = None


class Pageable(DTO):
    number: Optional[int] = None
    size: Optional[int] = None
    offset: Optional[int] = None
    sort: Optional[Sort] = None
    sorted: Optional[bool] = None

    def to_params(self) -> List[tuple]:
        """Make a list of paging parameters to be passed into a request."""
        params = []
        if self.size is not None:
            params.append(("size", self.size))
        if self.number is not None:
            params.append(("page", self.number))
        if self.sort is not None:
            for order in self.sort.orderBy or []:
                if order.property is None:
                    continue
                if order.direction is not None:
                    params.append(
                        ("sort", "{},{}".format(order.property, order.direction.value))
                    )
                else:
                    params.append(("sort", order.property))
        return params

    @classmethod
    def from_params(
        cls,
        size: Optional[int] = None,
        page: Optional[int] = None,
        sort_keys: Optional[List[str]] = None,
    ) -> "Pageable":
        """Make a Pageable instance from paging parameters.

        Sort keys may include a direction, e.g. ``"displayName,DESC"``.
        """
        pageable = cls()
        pageable.size = size
        pageable.number = page
        if sort_keys is not None:
            sort = Sort(orderBy=[])
            for sort_key in sort_keys:
                prop, _, direction = sort_key.partition(",")
                sort.orderBy.append(
                    Sort.Order(
                        property=prop,
                        direction=Sort.Order.Direction(direction.strip().upper())
                        if direction
                        else None,
                    )
                )
            pageable.sort = sort
        return pageable


class Page(DTO, Generic[T]):
    """A page of results from a paged FathomNet REST API endpoint."""

    content: List[T] = []
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    totalPages: Optional[int] = None
    totalItems: Optional[int] = None

    @classmethod
    def from_dict(cls, d: Any) -> "Page":
        # Servers that predate paging on an endpoint return a bare array: treat it as one complete page.
        if isinstance(d, list):
            d = {
                "content": d,
                "pageNumber": 0,
                "pageSize": len(d),
                "totalPages": 1,
                "totalItems": len(d),
            }
        return cls(**d)

    @property
    def is_last(self) -> bool:
        """Whether this is the last page of results."""
        if self.totalPages is None or self.pageNumber is None:
            return not self.content
        return self.pageNumber + 1 >= self.totalPages


class Roles(Enum):
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    READ = "READ"
    UNKNOWN = "UNKNOWN"
    UPDATE = "UPDATE"
    WRITE = "WRITE"


class Tag(DTO):
    uuid: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    mediaType: Optional[str] = None
    value: Optional[str] = None
    image: Optional[Image] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


class Taxa(DTO):
    name: Optional[str] = None
    rank: Optional[str] = None


class Badge(DTO):
    name: Optional[str] = None
    since: Optional[str] = None
    data: Optional[dict] = None


class BoundingBoxCommentContent(DTO):
    text: Optional[str] = None
    alternateConcept: Optional[str] = None


class BoundingBoxComment(DTO):
    uuid: Optional[str] = None
    boundingBoxUuid: Optional[str] = None
    email: Optional[str] = None
    text: Optional[str] = None
    alternateConcept: Optional[str] = None
    flagged: Optional[bool] = None
    created: Optional[str] = None
    lastUpdated: Optional[str] = None

    @property
    def createdTimestamp(self) -> Optional[str]:
        """Deprecated alias of ``created``."""
        return self.created

    @property
    def lastUpdatedTimestamp(self) -> Optional[str]:
        """Deprecated alias of ``lastUpdated``."""
        return self.lastUpdated


class Topic(DTO):
    topic: Optional[str] = None
    target: Optional[str] = None
    notification: Optional[bool] = None


class Activity(DTO):
    topic: Optional[Topic] = None
    attributedTo: Optional[str] = None
    lastUpdated: Optional[str] = None
    content: Optional[str] = None
    data: Optional[dict] = None


class FollowedTopic(Topic):
    uuid: Optional[str] = None
    email: Optional[str] = None
    created: Optional[str] = None
    lastUpdated: Optional[str] = None

    @property
    def createdTimestamp(self) -> Optional[str]:
        """Deprecated alias of ``created``."""
        return self.created

    @property
    def lastUpdatedTimestamp(self) -> Optional[str]:
        """Deprecated alias of ``lastUpdated``."""
        return self.lastUpdated


class FollowedTopics(DTO):
    email: Optional[str] = None
    followedTopics: Optional[List[FollowedTopic]] = None


class WormsNode(DTO):
    name: Optional[str] = None
    rank: Optional[str] = None
    aphiaId: Optional[int] = None
    acceptedAphiaId: Optional[int] = None
    alternateNames: Optional[List[str]] = None
    children: Optional[List["WormsNode"]] = None


class WormsNames(DTO):
    aphiaId: Optional[int] = None
    name: Optional[str] = None
    acceptedName: Optional[str] = None
    alternateNames: Optional[List[str]] = None


class ImageSetUploadPosition(DTO):
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    imageSetUploadUuid: Optional[str] = None


class ContributionStats(DTO):
    ownerInstitutionCode: Optional[str] = None
    totalUploads: Optional[int] = None
    totalImages: Optional[int] = None


class FullLicense(DTO):
    spdxId: Optional[str] = None
    name: Optional[str] = None
    url: Optional[str] = None
    selectableForImages: Optional[bool] = None
    selectableForAnnotations: Optional[bool] = None


class NotificationType(str, Enum):
    ACCOUNT_CREATED = "ACCOUNT_CREATED"
    IMAGE_SET = "IMAGE_SET"


class NotificationContent(DTO):
    notificationType: Optional[NotificationType] = None
    topic: Optional[str] = None
    message: Optional[str] = None
    email: Optional[str] = None


class Notification(DTO):
    uuid: Optional[str] = None
    notificationType: Optional[NotificationType] = None
    topic: Optional[str] = None
    message: Optional[str] = None
    email: Optional[str] = None
    createdTimestamp: Optional[str] = None
    readTimestamp: Optional[str] = None


class ImageSetUploadUpdate(DTO):
    contributorsEmail: Optional[str] = None
    contributorNotificationTimestamp: Optional[str] = None


class SimpleTag(DTO):
    key: Optional[str] = None
    value: Optional[str] = None
    mediaType: Optional[str] = None
