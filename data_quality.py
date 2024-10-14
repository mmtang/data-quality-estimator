'''
The Data Quality Estimator Tool describes the overall quality of a CEDEN data record by taking the QACode, ResultQualCode, ComplicanceCode, BatchVerificationCode, and special circumstances into account to assign it to one of the following data quality categories: 

0: MetaData, 1: Passed, 2: Some review needed, 3: Spatial accuracy unknown, 4: Extensive review needed, 5: Unknown data quality, 6: Reject record, 7: Error in data
(as of 1/22/18)

The assignments and categories are provisional. A working explanation of the data quality ranking can be found at the following link: https://docs.google.com/spreadsheets/d/1q-tGulvO9jyT2dR9GGROdy89z3W6xulYaci5-ezWAe0/edit?usp=sharing

Review the accompanying file, dq_constants.py, to see how each value in the quality check fields (e.g., QACode, ResultQualCode, BatchVerificationCode) are mapped to the data quality categories.

**********

The add_data_quality function below appends two fields to the existing CEDEN data structure:

1. DataQuality: The assigned data quality category (e.g., "Metadata", "Passed", "Extensive review needed") for the record

2. DataQualityIndicator: Explains the reason for the DataQuality value by indicating which quality assurance check the data did not pass (e.g. BatchVerificationCode, ResultQACode, etc.).

'''

import re
import dq_constants

# df = pandas dataframe
# data_type = 'benthic', 'chemistry', 'habitat',  'tissue', 'toxicity'
def add_data_quality(df, data_type):
    # Function for adding QACode data quality codes and scores to DQ dictionary
    def add_QACode(row):
        col = 'QACode'
        # for each value in the specific record
        # split the value up by commas and return a list
        # ie.  codeVal may be 'QAC,DNR,LOB' which is a string
        # this would return ['QAC', 'DNR', 'LOB'] which is an iterable list
        values = getattr(row, col).split(',')
        for i in values:
            try:
                DQ.append({'col': col, 'code': i, 'score': dq_constants.QA_Code_list[i]})
            except:
                print(i + ' not a valid key in QA_Code_list')

    def add_StationCode(row):
        col = 'StationCode'
        val = getattr(row, col)
        if bool(re.search('000NONPJ', str(val))):
            # if a record has 000NONPJ or any variant in the StationCode value, add 0 to DQ
            DQ.append({'col': col, 'code': '000NONPJ', 'score': 0})
        elif val in dq_constants.StationCode_list:
            DQ.append({'col': col, 'code': val, 'score': dq_constants.StationCode_list[val]})

    def add_Analyte(row):
        col = 'Analyte'
        val = getattr(row, col)
        # If the analyte name contains 'surrogate', mark DQ with a 0
        if bool(re.search('[Ss]urrogate', val)):
            DQ.append({'col': col, 'code': val, 'score': 0})

    def add_ResultQualCode(row):
        col = 'ResultQualCode'
        val = getattr(row, col)
        # special cases for ResQualCode
        year = getattr(row, 'SampleDate').year
        if val == 'DNQ' and year < 2008:
            DQ.append({'col': col, 'code': val, 'score': 6})
        elif val == 'ND' and data_type == 'benthic': # 8/30/24 - Changed this to add the data type
            # the Benthic dataset can have an ND value as long as the result
            # is not positive. Record is a pass if less than or equal to zero
            # reject if result is positive
            try:
                result = getattr(row, 'Result')
                if isinstance(result, (int, float)) and result > 0:
                    DQ.append({'col': col, 'code': val, 'score': 6}) # 8/30/24 -  Changed the score to 6 (reject)
                else:
                    DQ.append({'col': col, 'code': val, 'score': 1})
            except KeyError:
                DQ.append({'col': col, 'code': val, 'score': 1})
        # End of Special Rules for ResultQualCode
        # check each value in the code dictionary and add numerical value to DQ
        elif val in dq_constants.ResultQualCode_list:
            DQ.append({'col': col, 'code': val, 'score': dq_constants.ResultQualCode_list[val]})

    def add_Result(row):
        col = 'Result'
        val = getattr(row, col)
        # Results can be empty if ResultQualCode == 'ND'
        if val == '' and row['ResultQualCode'] == 'ND':
            DQ.append({'col': col, 'code': val, 'score': 1})
        else:
            # All other values, look up in code dictionary
            if val in dq_constants.Result_list:
                DQ.append({'col': col, 'code': val, 'score': dq_constants.Result_list[val]})

    def add_BatchVerification(row):
        try:
            col = 'BatchVerification'
            val = getattr(row, col)
            if val in dq_constants.BatchVerification_list:
                DQ.append({'col': col, 'code': val, 'score': dq_constants.BatchVerification_list[val]})
        except:
            pass

    def add_Latitude(row):
        col = 'TargetLatitude'
        val = getattr(row, col)
        if val in dq_constants.Latitude_list:
            DQ.append({'col': col, 'code': val, 'score': dq_constants.Latitude_list[val]})

    def add_SampleTypeCode(row):
        col = 'SampleTypeCode'
        val = getattr(row, col)
        if val in dq_constants.SampleTypeCode_list:
            DQ.append({'col': col, 'code': val, 'score': dq_constants.SampleTypeCode_list[val]})

    def add_SampleDate(row):
        col = 'SampleDate'
        val = getattr(row, col)
        year = val.year
        if year == 1950:
            DQ.append({'col': col, 'code': val, 'score': 0})

    def add_MatrixName(row):
        col = 'MatrixName'
        val = getattr(row, col)
        if val in dq_constants.MatrixName_list:
            DQ.append({'col': col, 'code': val, 'score': dq_constants.MatrixName_list[val]})

    def add_CollectionReplicate(row):
        col = 'CollectionReplicate'
        val = getattr(row, col)
        if val in dq_constants.CollectionReplicate_list:
            DQ.append({'col': col, 'code': val, 'score': dq_constants.CollectionReplicate_list[val]})

    def add_ResultsReplicate(row):
        try:
            col = 'ResultsReplicate'
            val = getattr(row, col)
            if val in dq_constants.ResultsReplicate_list:
                DQ.append({'col': col, 'code': val, 'score': dq_constants.ResultsReplicate_list[val]})
        except:
            pass

    def add_Datum(row):
        col = 'Datum'
        val = getattr(row, col)
        if val in dq_constants.Datum_list:
            DQ.append({'col': col, 'code': val, 'score': dq_constants.Datum_list[val]})
        
    for row in df.itertuples():
        # Initialize a list of dictionaries
        # ex. [{col: ###, code: ###, score: #}}, ...]
        DQ = []

        # Go through each column and append DQ dictionaries to DQ
        add_QACode(row)
        add_StationCode(row)
        add_Analyte(row)
        add_ResultQualCode(row)
        add_Result(row)
        add_BatchVerification(row)
        add_Latitude(row)
        add_SampleTypeCode(row)
        add_SampleDate(row)
        add_MatrixName(row)
        add_CollectionReplicate(row)
        add_ResultsReplicate(row)
        add_Datum(row)

        # A word about that DQ variable:
        # DQ might host a long list of numbers but if there is ever a zero, that whole
        # record should be classified as a QC record. If there isnt a zero and the
        # maximum value is a 1, then that record passed our data quality estimate
        # unblemished. If there isn't a zero and the max DQ values is greater than 1,
        # then ... we get the max value and store the corresponding value (from the
        # DQ_Codes dictionary, defined above). If the Max DQ is 6 (which is a reject
        # record) and QInd is empty, then this is a special rule case and we label it as
        # such. Otherwise, we throw all of the QInd information into the Quality
        # indicator column. QInd might look like:
        #   ['ResQualCode:npr,kqed', 'BatchVerificationCode:lol,btw,omg', ]
        # and the this gets converted and stored into the records new column called Data
        # Quality indicator a:
        # 'ResQualCode:npr,kqed; BatchVerificationCode:lol,btw,omg'

        # Find the min and max DQ scores
        min_DQ = min(i['score'] for i in DQ)
        max_DQ = max(i['score'] for i in DQ)

        # Determine the DQ variable for the data record
        if min_DQ == 0:
            df.at[row.Index, 'DataQuality'] = dq_constants.DQ_Codes[0]
            df.at[row.Index, 'DataQualityIndicator'] = ''
        elif max_DQ == 1:
            df.at[row.Index, 'DataQuality'] = dq_constants.DQ_Codes[1]
            df.at[row.Index, 'DataQualityIndicator'] = ''
        else:
            # Data quality score
            df.at[row.Index, 'DataQuality'] = dq_constants.DQ_Codes[max_DQ]

            # Data quality indicator:
            # iterate through all the code matches again and append all where score = max DQ to new list. This is in case there are mulitple codes sharing the same max DQ.
            equal_max_DQ = []
            for i in DQ:
                if i['score'] == max_DQ:
                    equal_max_DQ.append(i)

            # Initialize a new array to combine multiple codes into one string in case there are multiple codes per column
            joined_cols_codes = []
            unique_cols = set([i['col'] for i in equal_max_DQ])
            for col in unique_cols:
                codes = []
                # Append each code matching the column name to the codes array
                for i in equal_max_DQ:
                    if (i['col'] == col):
                        codes.append(i['code'])
                # Get unique values only (sorted)
                unique_codes = sorted(set(codes))
                # Join codes to form a single string
                code_string = ','.join(unique_codes)
                joined_cols_codes.append({'col': col, 'codes': code_string})

            # join array items to form the DQ indicator column value
            DQ_indicator = '; '.join(map(str, [i['col'] + ':' + i['codes'] for i in joined_cols_codes]))
            
            # write to record dictionary
            if max_DQ == 6 and DQ_indicator == '':
                df.at[row.Index, 'DataQualityIndicator'] = 'ResultQualCode Special Rules'
            else:
                df.at[row.Index, 'DataQualityIndicator'] = DQ_indicator

    # Return the dataframe with the added DQ columns
    return df