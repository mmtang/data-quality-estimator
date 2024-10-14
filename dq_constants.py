# DICTIONARIES
# The following dictionaries refer to codes and their corresponding data quality value as determined by
# Melissa Morris of SWRCB, Office of Information Management and Analysis. 

DQ_Codes = {0: "MetaData", 1: "Passed", 2: "Some review needed", 3: "Spatial accuracy unknown",
            4: "Extensive review needed", 5: "Unknown data quality", 6: "Reject record", 7: 'Error in data'}

# Some newer QA codes have not been added yet (they are currently skipped over): VFIRL, ROQ, H6, BRK
QA_Code_list = {"AWM": 1, "AY": 2, "BB": 2, "BBM": 2, "BCQ": 1, "BE": 2, "BH": 1, "BLM": 4, "BRKA": 2, "BS": 2,
                    "BT": 6, "BV": 2, "BX": 4, "BY": 4, "BZ": 4, "BZ15": 2, "C": 1, "CE": 4, "CIN": 2, "CJ": 2, "CNP": 2,
                    "CQA": 1, "CS": 2, "CSG": 2, "CT": 2, "CVH": 1, "CVHB": 4, "CVL": 1, "CVLB": 4, "CZM": 2, "D": 1,
                    "DB": 2, "DBLOD": 2, "DBM": 2, "DF": 2, "DG": 1, "DO": 1, "DRM": 2, "DS": 1, "DT": 1, "ERV": 4, "EUM": 4,
                    "EX": 4, "F": 2, "FCL": 2, "FDC": 2, "FDI": 2, "FDO": 6, "FDP": 2, "FDR": 1, "FDS": 1, "FEU": 6, "FIA": 6,
                    "FIB": 4, "FIF": 6, "FIO": 4, "FIP": 4, "FIT": 2, "FIV": 6, "FLV": 2, "FNM": 6, "FO": 2, "FS": 6, "FTD": 6,
                    "FTT": 6, "FUD": 6, "FX": 4, "GB": 2, "GBC": 4, "GC": 1, "GCA": 1, "GD": 1, "GN": 4, "GR": 4, "H": 2, "H22": 4,
                    "H24": 4, "H8": 2, "HB": 2, "HD": 4, "HH": 2, "HNO2": 2, "HR": 1, "HS": 4, "HT": 1, "IE": 2, "IF": 2, "IL": 4,
                    "ILM": 2, "ILN": 2, "ILO": 2, "IM": 2, "IP": 4, "IP5": 4, "IPMDL2": 4, "IPMDL3": 4, "IPRL": 4, "IS": 4,
                    "IU": 4, "IZM": 2, "J": 2, "JA": 2, "JDL": 2, "LB": 2, "LC": 4, "LRGN": 6, "LRIL": 6, "LRIP": 6, "LRIU": 6,
                    "LRJ": 6, "LRJA": 6, "LRM": 6, "LRQ": 6, "LST": 6, "M": 2, "MAL": 1, "MN": 4, "N": 2, "NAS": 2, "NBC": 2,
                    "NC": 1, "NG": 1, "NMDL": 1, "None": 1, "NR": 5, "NRL": 1, "NTR": 1, "OA": 2, "OV": 2, "P": 4, "PG": 4,
                    "PI": 4, "PJ": 1, "PJM": 1, "PJN": 1, "PP": 4, "PRM": 4, "Q": 4, "QAX": 1, "QG": 4, "R": 6, "RE": 1, "REL": 1,
                    "RIP": 6, "RIU": 6, "RJ": 6, "RLST": 6, "RPV": 4, "RQ": 2, "RU": 4, "RY": 4, "SC": 1, "SCR": 2, "SLM": 1, "TA": 4,
                    "TAC": 1, "TC": 4, "TCI": 4, "TCT": 4, "TD": 4, "TH": 4, "THS": 4, "TK": 4, "TL": 2, "TNC": 2, "TNS": 1, "TOQ": 4,
                    "TP": 4, "TR": 6, "TS": 4, "TW": 2, "UF": 2, "UJ": 2, "UKM": 4, "ULM": 4, "UOL": 2, "VCQ": 2, "VQN": 2, "VC": 2,
                    "VBB": 2, "VBS": 2, "VBY": 4, "VBZ": 4, "VBZ15": 2, "VCJ": 2, "VCO": 2, "VCR": 2, "VD": 1, "VDO": 1, "VDS": 1,
                    "VELB": 1, "VEUM": 4, "VFDP": 2, "VFIF": 6, "VFNM": 6, "VFO": 2, "VGB": 2, "VGBC": 4, "VGN": 4, "VH": 2, "VH24": 4,
                    "VH8": 2, "VHB": 2, "VIE": 2, "VIL": 4, "VILN": 4, "VILO": 2, "VIP": 4, "VIP5": 4, "VIPMDL2": 4, "VIPMDL3": 4,
                    "VIPRL": 4, "VIS": 4, "VIU": 4, "VJ": 2, "VJA": 2, "VLB": 2, "VLMQO": 2, "VM": 2, "VNBC": 2, "VNC": 1, "VNMDL": 1,
                    "VNTR": 1, "VPJM": 1, "VPMQO": 2, "VQAX": 1, "VQCA": 4, "VQCP": 4, "VR": 6, "VRBS": 6, "VRBZ": 6, "VRDO": 6,
                    "VRE": 1, "VREL": 1, "VRGN": 6, "VRIL": 6, "VRIP": 6, "VRIU": 6, "VRJ": 6, "VRLB": 6, "VRLST": 6, "VRQ": 2,
                    "VRVQ": 6, "VS": 2, "VSC": 1, "VSCR": 2, "VSD3": 1, "VTAC": 1, "VTCI": 4, "VTCT": 4, "VTNC": 2, "VTOQ": 4, "VTR": 6,
                    "VTW": 4, "VVQ": 6, "WOQ": 4,  }

BatchVerification_list = {"NA": 5, "NR": 5, "VAC": 1, "VAC,VCN": 6, "VAC,VMD": 2, "VAC,VMD,VQI": 4,
                                  "VAC,VQI": 4, "VAC,VR": 6, "VAF": 1, "VAF,VMD": 2, "VAF,VQI": 4, "VAP": 1,
                                  "VAP,VI": 4, "VAP,VQI": 4, "VCN": 6, "VLC": 1, "VLC,VMD": 2, "VLC,VMD,VQI": 4,
                                  "VLC,VQI": 4, "VLF": 1, "VMD": 2, "VQI": 4, "VQI,VTC": 4, "VQN": 5, "VR": 6, "VTC": 2}

ResultQualCode_list = {"/oC": 4, "<": 1, "<=": 1, "=": 1, ">": 1, ">=": 1, "A": 1, "CG": 4, "COL": 1, "DNQ": 2,
                           "JF": 1, "NA": 6, "ND": 1, "NR": 6, "NRS": 6, "NRT": 6, "NSI": 1, "P": 1, "PA": 1, "w/C": 4,
                           "": 1, "Systematic Contamination": 4, }

Latitude_list = {"-88": 0, "": 6, '0.0': 6, -88: 0, 'NaN': 6 }

Result_list = {"": 1, 
}

StationCode_list = {"LABQA": 0, "LABQA_SWAMP": 0, "000NONPJ": 0, "FIELDQA": 0, "Non Project QA Sample": 0,
                    "Laboratory QA Sample": 0, "Field QA sample": 0, "FIELDQA SWAMP": 0, "000NONSW": 0, "FIELDQA_SWAMP": 0}

SampleTypeCode_list = {"LabBlank": 0, "CompBLDup": 0, "LCS": 0, "CRM": 0, "FieldBLDup_Grab": 0, "FieldBLDup_Int": 0,
                        "FieldBLDup": 0, "FieldBlank": 0, "TravelBlank": 0, "EquipBlank": 0, "DLBlank": 0,
                        "FilterBlank": 0, "MS1": 0, "MS2": 0, "MS3": 0, "MSBLDup": 0, }

SampleDate_list = {"Jan  1 1950 12:00AM": 0, }

MatrixName_list = {"blankwater": 0, "Blankwater": 0, "labwater": 0, "blankmatrix": 0, }

CollectionReplicate_list = {"0": 1, "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, }

ResultsReplicate_list = {"0": 1, "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, }

Datum_list = {"NR": 3, }

# Dictionary of dictionaries
CodeColumns = {
    "QACode": QA_Code_list,
    "BatchVerification": BatchVerification_list,
    "ResultQualCode": ResultQualCode_list,
    "TargetLatitude": Latitude_list,
    "Result": Result_list,
    "StationCode": StationCode_list,
    "SampleTypeCode": SampleTypeCode_list,
    "SampleDate": SampleDate_list,
    "MatrixName": MatrixName_list,
    "CollectionReplicate": CollectionReplicate_list,
    "ResultsReplicate": ResultsReplicate_list,
    "Datum": Datum_list
}