# dto.py (fathomnet-py)
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum
from typing import List, Optional
from requests.auth import AuthBase
from lxml import etree
from lxml.builder import E
import os


@dataclass_json
@dataclass
class AImageDTO:
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
    tags: Optional[List['ATagDTO']] = None
    timestamp: Optional[str] = None
    width: Optional[int] = None
    boundingBoxes: Optional[List['ABoundingBoxDTO']] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None

    def to_pascal_voc(self, path: Optional[str] = None, pretty_print: bool = False) -> str:
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
                raise ValueError('Either the path argument or the image URL must be specified.')
            path = self.url

        # Parse the folder name and file name
        dir_path, base_name = os.path.split(path)
        folder_name = os.path.basename(dir_path)

        # Encode bounding box data into object tags
        boxes = self.boundingBoxes or []
        objects = [
            E.object(
                E.name(box.concept + (' {}'.format(box.altConcept) if box.altConcept is not None else '')),
                E.pose('Unspecified'),
                E.truncated(str(int(box.truncated) if box.truncated is not None else 0)),
                E.difficult('0'),
                E.occluded(str(int(box.occluded) if box.occluded is not None else 0)),
                E.bndbox(
                    E.xmin(str(box.x)),
                    E.xmax(str(box.x + box.width)),
                    E.ymin(str(box.y)),
                    E.ymax(str(box.y + box.height))
                )
            )
            for box in boxes
        ]

        # Encode annotation data
        annotation = E.annotation(
            E.folder(folder_name),
            E.filename(base_name),
            E.path(path),
            E.source(
                E.database('FathomNet')
            ),
            E.size(
                E.width(str(self.width)),
                E.height(str(self.height)),
                E.depth('3')
            ),
            E.segmented('0'),
            *objects
        )

        return etree.tostring(annotation, pretty_print=pretty_print).decode()


@dataclass_json
@dataclass
class ATagDTO:
    id: Optional[int] = None
    uuid: Optional[str] = None
    key: Optional[str] = None
    mediaType: Optional[str] = None
    value: Optional[str] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None
    image: Optional[AImageDTO] = None


@dataclass_json
@dataclass
class TagDTO(ATagDTO):
    imageUuid: Optional[str] = None


@dataclass_json
@dataclass
class ABoundingBoxDTO:
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
    verified: Optional[bool] = None
    verifier: Optional[str] = None
    verificationTimestamp: Optional[str] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


@dataclass_json
@dataclass
class ApiKey:
    uuid: Optional[str] = None
    apiKey: Optional[str] = None


@dataclass_json
@dataclass
class AuthHeader(AuthBase):
    type: Optional[str] = None
    token: Optional[str] = None

    @property
    def auth_dict(self):
        return {'Authorization': '{} {}'.format(self.type, self.token)}

    def __call__(self, r):
        r.headers.update(self.auth_dict)
        return r


@dataclass_json
@dataclass
class Authentication:
    attributes: Optional[object] = None


@dataclass_json
@dataclass
class BoundingBoxDTO(ABoundingBoxDTO):
    imageUuid: Optional[str] = None


@dataclass_json
@dataclass
class BoundingBox:
    uuid: Optional[str] = None
    id: Optional[int] = None
    userDefinedKey: Optional[str] = None
    concept: Optional[str] = None
    altConcept: Optional[str] = None
    image: Optional['Image'] = None
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
    verified: Optional[bool] = None
    verifier: Optional[str] = None
    verificationTimestamp: Optional[str] = None


@dataclass_json
@dataclass
class ByConceptCount:
    concept: Optional[str] = None
    count: Optional[int] = None


@dataclass_json
@dataclass
class ByContributorCount:
    contributorsEmail: Optional[str] = None
    count: Optional[int] = None


@dataclass_json
@dataclass
class BDarwinCore:
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


@dataclass_json
@dataclass
class BImageSetUploadDTO:
    uuid: Optional[str] = None
    localPath: Optional[str] = None
    remoteUri: Optional[str] = None
    sha256: Optional[str] = None
    format: Optional['ImageSetUpload.UploadFormat'] = None
    contributorsEmail: Optional[str] = None
    status: Optional['ImageSetUpload.Status'] = None
    statusUpdaterEmail: Optional[str] = None
    statusUpdateTimestamp: Optional[str] = None
    rejectionReason: Optional[str] = None
    rejectionDetails: Optional[str] = None
    darwinCore: Optional[BDarwinCore] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


@dataclass_json
@dataclass
class Count:
    objectType: Optional[str] = None
    count: Optional[int] = None


@dataclass_json
@dataclass
class DarwinCore:
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
    imageSetUpload: Optional['ImageSetUpload'] = None


@dataclass_json
@dataclass
class FathomnetIdAdminMutation:
    disabled: Optional[bool] = None
    expertiseRank: Optional[str] = None
    roleData: Optional[str] = None
    organization: Optional[str] = None


@dataclass_json
@dataclass
class FathomnetIdMutation:
    jobTitle: Optional[str] = None
    organization: Optional[str] = None
    profile: Optional[str] = None
    displayName: Optional[str] = None


@dataclass_json
@dataclass
class FathomnetIdentity:
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
    roles: Optional[List['Roles']] = None
    orcid: Optional[str] = None
    notificationFrequency: Optional[str] = None


@dataclass_json
@dataclass
class GeoImage:
    uuid: Optional[str] = None
    url: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    depthMeters: Optional[float] = None
    contributorsEmail: Optional[str] = None
    timestamp: Optional[str] = None
    valid: Optional[bool] = None
    lastValidation: Optional[str] = None


@dataclass_json
@dataclass
class GeoImageConstraints:
    concept: Optional[str] = None
    taxaProviderName: Optional[str] = None
    contributorsEmail: Optional[str] = None
    startTimestamp: Optional[str] = None
    endTimestamp: Optional[str] = None
    imagingTypes: Optional[List[str]] = None
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


@dataclass_json
@dataclass
class GeoImageConstraintsCount:
    constraints: Optional[GeoImageConstraints] = None
    count: Optional[int] = None


@dataclass_json
@dataclass
class Image:
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
    tags: Optional[List['Tag']] = None
    boundingBoxes: Optional[List[BoundingBox]] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None
    imageSetUploads: Optional[List['ImageSetUpload']] = None


@dataclass_json
@dataclass
class ImageSetUpload:
    class Status(Enum):
        PENDING = 'PENDING'
        ACCEPTED = 'ACCEPTED'
        REJECTED = 'REJECTED'

    class UploadFormat(Enum):
        CSV = 'CSV'
        UNSUPPORTED = 'UNSUPPORTED'

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
    format: Optional[UploadFormat] = None
    darwinCore: Optional[DarwinCore] = None
    images: Optional[List[Image]] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


@dataclass_json
@dataclass
class ImageSetUploadStats:
    imageSetUploadUuid: Optional[str] = None
    imageCount: Optional[int] = None
    boundingBoxCount: Optional[int] = None
    verifiedBoundingBoxCount: Optional[int] = None


@dataclass_json
@dataclass
class MarineRegion:
    id: Optional[int] = None
    MRGID: Optional[int] = None
    name: Optional[str] = None
    minLatitude: Optional[float] = None
    maxLatitude: Optional[float] = None
    minLongitude: Optional[float] = None
    maxLongitude: Optional[float] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


@dataclass_json
@dataclass
class Message:
    message: Optional[str] = None


@dataclass_json
@dataclass
class Sort:
    @dataclass_json
    @dataclass
    class Order:
        class Direction(Enum):
            ASC = 'ASC'
            DESC = 'DESC'

        ignoreCase: Optional[bool] = None
        direction: Optional[Direction] = None
        property: Optional[str] = None
        ascending: Optional[bool] = None

    sorted: Optional[bool] = None
    orderBy: Optional[List[Order]] = None


@dataclass_json
@dataclass
class Pageable:
    number: Optional[int] = None
    size: Optional[int] = None
    offset: Optional[int] = None
    sort: Optional[Sort] = None
    sorted: Optional[bool] = None

    def to_params(self) -> List[tuple]:
        """Make a list of paging parameters to be passed into a request."""
        params = []
        if self.size is not None:
            params.append(('size', self.size))
        if self.number is not None:
            params.append(('page', self.number))
        if self.sort is not None:
            for order in self.sort.orderBy:
                params.append(('sort', order.property))
        return params

    @classmethod
    def from_params(cls, size: Optional[int] = None, page: Optional[int] = None, sort_keys: Optional[List[str]] = None):
        """Make a Pageable instance from paging parameters."""
        pageable = cls()
        pageable.size = size
        pageable.number = page
        if sort_keys is not None:
            sort = Sort(orderBy=[])
            for sort_key in sort_keys:
                sort.orderBy.append(Sort.Order(property=sort_key))
            pageable.sort = sort


class Roles(Enum):
    ADMIN = 'ADMIN'
    MODERATOR = 'MODERATOR'
    READ = 'READ'
    UNKNOWN = 'UNKNOWN'
    UPDATE = 'UPDATE'
    WRITE = 'WRITE'


@dataclass_json
@dataclass
class Tag:
    uuid: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    mediaType: Optional[str] = None
    value: Optional[str] = None
    image: Optional[Image] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


@dataclass_json
@dataclass
class Taxa:
    name: Optional[str] = None
    rank: Optional[str] = None


@dataclass_json
@dataclass
class Badge:
    name: Optional[str] = None
    since: Optional[str] = None
    data: Optional[dict] = None


@dataclass_json
@dataclass
class BoundingBoxCommentContent:
    text: Optional[str] = None
    alternateConcept: Optional[str] = None


@dataclass_json
@dataclass
class BoundingBoxComment:
    uuid: Optional[str] = None
    boundingBoxUuid: Optional[str] = None
    email: Optional[str] = None
    text: Optional[str] = None
    alternateConcept: Optional[str] = None
    flagged: Optional[bool] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


@dataclass_json
@dataclass
class Topic:
    topic: Optional[str] = None
    target: Optional[str] = None
    notification: Optional[bool] = None


@dataclass_json
@dataclass
class Activity:
    topic: Optional[Topic] = None
    attributedTo: Optional[str] = None
    lastUpdated: Optional[str] = None
    content: Optional[str] = None
    data: Optional[dict] = None


@dataclass_json
@dataclass
class FollowedTopic(Topic):
    uuid: Optional[str] = None
    email: Optional[str] = None
    createdTimestamp: Optional[str] = None
    lastUpdatedTimestamp: Optional[str] = None


@dataclass_json
@dataclass
class WormsNode:
    name: Optional[str] = None
    rank: Optional[str] = None
    apiaId: Optional[int] = None
    alternateNames: Optional[List[str]] = None
    children: Optional[List['WormsNode']] = None
