from dataclasses import dataclass, field
from typing import List, Optional, TypedDict, NotRequired
from .hc_enums import DocType

@dataclass
class ApiResponse(TypedDict):
    filenumber: NotRequired[str]
    message: str
    error: int
    success: bool


@dataclass
class DocFile:
    doctype: Optional[DocType] = None
    dateadded: Optional[str] = None
    user: Optional[str] = None
    notes: Optional[str] = None
    filename: Optional[str] = None

@dataclass
class LogTrail:
    date: Optional[str] = None
    activity: Optional[str] = None
    user: Optional[str] = None

@dataclass
class Claim:
    filenumber: Optional[int] = None
    customername: Optional[str] = None
    clientclaimno: Optional[str] = None
    rentername: Optional[str] = None
    ranumber: Optional[str] = None
    insuredname: Optional[str] = None
    insurancecompany: Optional[str] = None
    claimnumber: Optional[str] = None
    policynumber: Optional[str] = None
    dateofloss: Optional[str] = None
    adjuster: Optional[str] = None
    adjusterphone: Optional[str] = None
    firstparty: Optional[bool] = None
    thirdparty: Optional[bool] = None
    cdw: Optional[bool] = None
    hc_adj: Optional[str] = None
    officephone: Optional[str] = None
    email: Optional[str] = None
    vin: Optional[str] = None
    vehyear: Optional[int] = None
    vehmake: Optional[str] = None
    vehmodel: Optional[str] = None
    vehedition: Optional[str] = None
    color: Optional[str] = None
    platenumber: Optional[str] = None
    unitnumber: Optional[str] = None
    inspectiondate: Optional[str] = None
    estimateamount: Optional[float] = None
    totalloss: Optional[bool] = None
    continuedrentalamt: Optional[float] = None
    dv_amt: Optional[float] = None
    liabilityaccepted: Optional[bool] = None
    liabilitydenied: Optional[bool] = None
    settlement_pd: Optional[float] = None
    settlement_salvage: Optional[float] = None
    settlement_cr: Optional[float] = None
    settlement_dv: Optional[float] = None
    settlement_other: Optional[float] = None
    settlement_deductable: Optional[float] = None
    administrativefee: Optional[float] = None
    appraisalfee: Optional[float] = None
    datefileclosed: Optional[str] = None
    settlementoffer: Optional[float] = None
    supplement: Optional[str] = None
    settlementtowing: Optional[float] = None
    settlementstorage: Optional[float] = None
    demand_admin_fee: Optional[float] = None
    demand_appraisal_fee: Optional[float] = None
    estimatedate: Optional[str] = None
    demanddate: Optional[str] = None
    policystartdate: Optional[str] = None
    policyenddate: Optional[str] = None
    vehicleowner: Optional[str] = None
    docfiles: List[DocFile] = field(default_factory=list)
    logtrail: List[LogTrail] = field(default_factory=list)
