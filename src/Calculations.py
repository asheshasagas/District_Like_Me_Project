def total_enrollments(data):
    import numpy as np
    # Enrollment columns in separate list
    enrollment_columns = []
    for column in data.columns:
        if "_1819" in column:
            enrollment_columns.append(column)
    # Calculate the Total Enrollment for School Districts per subgroup
    data["American_Indian"] = data.fillna(0)['amerindian0_1819'] + data.fillna(0)['amerindian1_1819'] + \
                              data.fillna(0)['amerindian2_1819'] + data.fillna(0)['amerindian3_1819'] + \
                              data.fillna(0)['amerindian4_1819'] + data.fillna(0)['amerindian5_1819'] + \
                              data.fillna(0)['amerindian6_1819'] + data.fillna(0)['amerindian7_1819'] + \
                              data.fillna(0)['amerindian8_1819'] + data.fillna(0)['amerindian9_1819'] + \
                              data.fillna(0)['amerindian10_1819'] + data.fillna(0)['amerindian11_1819'] + \
                              data.fillna(0)['amerindian12_1819'] + data.fillna(0)['amerindian13_1819'] + \
                              data.fillna(0)['amerindian14_1819']
    data["Asian"] = data.fillna(0)['asian0_1819'] + data.fillna(0)['asian1_1819'] + data.fillna(0)['asian2_1819'] + \
                    data.fillna(0)['asian3_1819'] + data.fillna(0)['asian4_1819'] + data.fillna(0)['asian5_1819'] + \
                    data.fillna(0)['asian6_1819'] + data.fillna(0)['asian7_1819'] + data.fillna(0)['asian8_1819'] + \
                    data.fillna(0)['asian9_1819'] + data.fillna(0)['asian10_1819'] + data.fillna(0)['asian11_1819'] + \
                    data.fillna(0)['asian12_1819'] + data.fillna(0)['asian13_1819'] + data.fillna(0)['asian14_1819']
    data["Black_or_African_American"] = data.fillna(0)['black0_1819'] + data.fillna(0)['black1_1819'] + \
                                        data.fillna(0)['black2_1819'] + data.fillna(0)['black3_1819'] + \
                                        data.fillna(0)['black4_1819'] + data.fillna(0)['black5_1819'] + \
                                        data.fillna(0)['black6_1819'] + data.fillna(0)['black7_1819'] + \
                                        data.fillna(0)['black8_1819'] + data.fillna(0)['black9_1819'] + \
                                        data.fillna(0)['black10_1819'] + data.fillna(0)['black11_1819'] + \
                                        data.fillna(0)['black12_1819'] + data.fillna(0)['black13_1819'] + \
                                        data.fillna(0)['black14_1819']
    data["Hispanic_or_Latino"] = data.fillna(0)['hispanic0_1819'] + data.fillna(0)['hispanic1_1819'] + \
                                 data.fillna(0)['hispanic2_1819'] + data.fillna(0)['hispanic3_1819'] + \
                                 data.fillna(0)['hispanic4_1819'] + data.fillna(0)['hispanic5_1819'] + \
                                 data.fillna(0)['hispanic6_1819'] + data.fillna(0)['hispanic7_1819'] + \
                                 data.fillna(0)['hispanic8_1819'] + data.fillna(0)['hispanic9_1819'] + \
                                 data.fillna(0)['hispanic10_1819'] + data.fillna(0)['hispanic11_1819'] + \
                                 data.fillna(0)['hispanic12_1819'] + data.fillna(0)['hispanic13_1819'] + \
                                 data.fillna(0)['hispanic14_1819']
    data["Hawaiian"] = data.fillna(0)['hawaiian0_1819'] + data.fillna(0)['hawaiian1_1819'] + \
                       data.fillna(0)['hawaiian2_1819'] + data.fillna(0)['hawaiian3_1819'] + \
                       data.fillna(0)['hawaiian4_1819'] + data.fillna(0)['hawaiian5_1819'] + \
                       data.fillna(0)['hawaiian6_1819'] + data.fillna(0)['hawaiian7_1819'] + \
                       data.fillna(0)['hawaiian8_1819'] + data.fillna(0)['hawaiian9_1819'] + \
                       data.fillna(0)['hawaiian10_1819'] + data.fillna(0)['hawaiian11_1819'] + \
                       data.fillna(0)['hawaiian12_1819'] + data.fillna(0)['hawaiian13_1819'] + \
                       data.fillna(0)['hawaiian14_1819']
    data["Not_Specified"] = data.fillna(0)['notspecified0_1819'] + data.fillna(0)['notspecified1_1819'] + \
                            data.fillna(0)['notspecified2_1819'] + data.fillna(0)['notspecified3_1819'] + \
                            data.fillna(0)['notspecified4_1819'] + data.fillna(0)['notspecified5_1819'] + \
                            data.fillna(0)['notspecified6_1819'] + data.fillna(0)['notspecified7_1819'] + \
                            data.fillna(0)['notspecified8_1819'] + data.fillna(0)['notspecified9_1819'] + \
                            data.fillna(0)['notspecified10_1819'] + data.fillna(0)['notspecified11_1819'] + \
                            data.fillna(0)['notspecified12_1819'] + data.fillna(0)['notspecified13_1819'] + \
                            data.fillna(0)['notspecified14_1819']
    data["Multi_Racial"] = data.fillna(0)['multiracial0_1819'] + data.fillna(0)['multiracial1_1819'] + data.fillna(0)[
        'multiracial2_1819'] + data.fillna(0)['multiracial3_1819'] + data.fillna(0)['multiracial4_1819'] + \
                           data.fillna(0)['multiracial5_1819'] + data.fillna(0)['multiracial6_1819'] + \
                           data.fillna(0)['multiracial7_1819'] + data.fillna(0)['multiracial8_1819'] + \
                           data.fillna(0)['multiracial9_1819'] + data.fillna(0)['multiracial10_1819'] + \
                           data.fillna(0)['multiracial11_1819'] + data.fillna(0)['multiracial12_1819'] + \
                           data.fillna(0)['multiracial13_1819'] + data.fillna(0)['multiracial14_1819']
    data["White"] = data.fillna(0)['white0_1819'] + data.fillna(0)['white1_1819'] + data.fillna(0)['white2_1819'] + \
                    data.fillna(0)['white3_1819'] + data.fillna(0)['white4_1819'] + data.fillna(0)['white5_1819'] + \
                    data.fillna(0)['white6_1819'] + data.fillna(0)['white7_1819'] + data.fillna(0)['white8_1819'] + \
                    data.fillna(0)['white9_1819'] + data.fillna(0)['white10_1819'] + data.fillna(0)['white11_1819'] + \
                    data.fillna(0)['white12_1819'] + data.fillna(0)['white13_1819'] + data.fillna(0)['white14_1819']
    data["Total_Enrollment"] = data.fillna(0)['grade0_total_1819'] + data.fillna(0)['grade1_total_1819'] + \
                               data.fillna(0)['grade2_total_1819'] + data.fillna(0)['grade3_total_1819'] + \
                               data.fillna(0)['grade4_total_1819'] + data.fillna(0)['grade5_total_1819'] + \
                               data.fillna(0)['grade6_total_1819'] + data.fillna(0)['grade7_total_1819'] + \
                               data.fillna(0)['grade8_total_1819'] + data.fillna(0)['grade9_total_1819'] + \
                               data.fillna(0)['grade10_total_1819'] + data.fillna(0)['grade11_total_1819'] + \
                               data.fillna(0)['grade12_total_1819'] + data.fillna(0)['grade13_total_1819'] + \
                               data.fillna(0)['grade14_total_1819']

    # Mark the nulls in Total enrollment columns for each subgroup
    for i in range(len(data)):
        if (np.isnan(data['amerindian0_1819'][i]) == True) & (np.isnan(data['amerindian1_1819'][i]) == True) & (
                np.isnan(data['amerindian2_1819'][i]) == True) & (np.isnan(data['amerindian3_1819'][i]) == True) & (
                np.isnan(data['amerindian4_1819'][i]) == True) & (np.isnan(data['amerindian5_1819'][i]) == True) & (
                np.isnan(data['amerindian6_1819'][i]) == True) & (np.isnan(data['amerindian7_1819'][i]) == True) & (
                np.isnan(data['amerindian8_1819'][i]) == True) & (np.isnan(data['amerindian9_1819'][i]) == True) & (
                np.isnan(data['amerindian10_1819'][i]) == True) & (np.isnan(data['amerindian11_1819'][i]) == True) & (
                np.isnan(data['amerindian12_1819'][i]) == True) & (np.isnan(data['amerindian13_1819'][i]) == True) & (
                np.isnan(data['amerindian14_1819'][i]) == True):
            data['American_Indian'][i] = np.nan
        if (np.isnan(data['asian0_1819'][i]) == True) & (np.isnan(data['asian1_1819'][i]) == True) & (
                np.isnan(data['asian2_1819'][i]) == True) & (np.isnan(data['asian3_1819'][i]) == True) & (
                np.isnan(data['asian4_1819'][i]) == True) & (np.isnan(data['asian5_1819'][i]) == True) & (
                np.isnan(data['asian6_1819'][i]) == True) & (np.isnan(data['asian7_1819'][i]) == True) & (
                np.isnan(data['asian8_1819'][i]) == True) & (np.isnan(data['asian9_1819'][i]) == True) & (
                np.isnan(data['asian10_1819'][i]) == True) & (np.isnan(data['asian11_1819'][i]) == True) & (
                np.isnan(data['asian12_1819'][i]) == True) & (np.isnan(data['asian13_1819'][i]) == True) & (
                np.isnan(data['asian14_1819'][i]) == True):
            data['Asian'][i] = np.nan
        if (np.isnan(data['black0_1819'][i]) == True) & (np.isnan(data['black1_1819'][i]) == True) & (
                np.isnan(data['black2_1819'][i]) == True) & (np.isnan(data['black3_1819'][i]) == True) & (
                np.isnan(data['black4_1819'][i]) == True) & (np.isnan(data['black5_1819'][i]) == True) & (
                np.isnan(data['black6_1819'][i]) == True) & (np.isnan(data['black7_1819'][i]) == True) & (
                np.isnan(data['black8_1819'][i]) == True) & (np.isnan(data['black9_1819'][i]) == True) & (
                np.isnan(data['black10_1819'][i]) == True) & (np.isnan(data['black11_1819'][i]) == True) & (
                np.isnan(data['black12_1819'][i]) == True) & (np.isnan(data['black13_1819'][i]) == True) & (
                np.isnan(data['black14_1819'][i]) == True):
            data['Black_or_African_American'][i] = np.nan
        if (np.isnan(data['hispanic0_1819'][i]) == True) & (np.isnan(data['hispanic1_1819'][i]) == True) & (
                np.isnan(data['hispanic2_1819'][i]) == True) & (np.isnan(data['hispanic3_1819'][i]) == True) & (
                np.isnan(data['hispanic4_1819'][i]) == True) & (np.isnan(data['hispanic5_1819'][i]) == True) & (
                np.isnan(data['hispanic6_1819'][i]) == True) & (np.isnan(data['hispanic7_1819'][i]) == True) & (
                np.isnan(data['hispanic8_1819'][i]) == True) & (np.isnan(data['hispanic9_1819'][i]) == True) & (
                np.isnan(data['hispanic10_1819'][i]) == True) & (np.isnan(data['hispanic11_1819'][i]) == True) & (
                np.isnan(data['hispanic12_1819'][i]) == True) & (np.isnan(data['hispanic13_1819'][i]) == True) & (
                np.isnan(data['hispanic14_1819'][i]) == True):
            data['Hispanic_or_Latino'][i] = np.nan
        if (np.isnan(data['hawaiian0_1819'][i]) == True) & (np.isnan(data['hawaiian1_1819'][i]) == True) & (
                np.isnan(data['hawaiian2_1819'][i]) == True) & (np.isnan(data['hawaiian3_1819'][i]) == True) & (
                np.isnan(data['hawaiian4_1819'][i]) == True) & (np.isnan(data['hawaiian5_1819'][i]) == True) & (
                np.isnan(data['hawaiian6_1819'][i]) == True) & (np.isnan(data['hawaiian7_1819'][i]) == True) & (
                np.isnan(data['hawaiian8_1819'][i]) == True) & (np.isnan(data['hawaiian9_1819'][i]) == True) & (
                np.isnan(data['hawaiian10_1819'][i]) == True) & (np.isnan(data['hawaiian11_1819'][i]) == True) & (
                np.isnan(data['hawaiian12_1819'][i]) == True) & (np.isnan(data['hawaiian13_1819'][i]) == True) & (
                np.isnan(data['hawaiian14_1819'][i]) == True):
            data['Hawaiian'][i] = np.nan
        if (np.isnan(data['notspecified0_1819'][i]) == True) & (np.isnan(data['notspecified1_1819'][i]) == True) & (
                np.isnan(data['notspecified2_1819'][i]) == True) & (np.isnan(data['notspecified3_1819'][i]) == True) & (
                np.isnan(data['notspecified4_1819'][i]) == True) & (np.isnan(data['notspecified5_1819'][i]) == True) & (
                np.isnan(data['notspecified6_1819'][i]) == True) & (np.isnan(data['notspecified7_1819'][i]) == True) & (
                np.isnan(data['notspecified8_1819'][i]) == True) & (np.isnan(data['notspecified9_1819'][i]) == True) & (
                np.isnan(data['notspecified10_1819'][i]) == True) & (
                np.isnan(data['notspecified11_1819'][i]) == True) & (
                np.isnan(data['notspecified12_1819'][i]) == True) & (
                np.isnan(data['notspecified13_1819'][i]) == True) & (
                np.isnan(data['notspecified14_1819'][i]) == True):
            data['Not_Specified'][i] = np.nan
        if (np.isnan(data['multiracial0_1819'][i]) == True) & (np.isnan(data['multiracial1_1819'][i]) == True) & (
                np.isnan(data['multiracial2_1819'][i]) == True) & (np.isnan(data['multiracial3_1819'][i]) == True) & (
                np.isnan(data['multiracial4_1819'][i]) == True) & (np.isnan(data['multiracial5_1819'][i]) == True) & (
                np.isnan(data['multiracial6_1819'][i]) == True) & (np.isnan(data['multiracial7_1819'][i]) == True) & (
                np.isnan(data['multiracial8_1819'][i]) == True) & (np.isnan(data['multiracial9_1819'][i]) == True) & (
                np.isnan(data['multiracial10_1819'][i]) == True) & (np.isnan(data['multiracial11_1819'][i]) == True) & (
                np.isnan(data['multiracial12_1819'][i]) == True) & (np.isnan(data['multiracial13_1819'][i]) == True) & (
                np.isnan(data['multiracial14_1819'][i]) == True):
            data['Multi_Racial'][i] = np.nan
        if (np.isnan(data['white0_1819'][i]) == True) & (np.isnan(data['white1_1819'][i]) == True) & (
                np.isnan(data['white2_1819'][i]) == True) & (np.isnan(data['white3_1819'][i]) == True) & (
                np.isnan(data['white4_1819'][i]) == True) & (np.isnan(data['white5_1819'][i]) == True) & (
                np.isnan(data['white6_1819'][i]) == True) & (np.isnan(data['white7_1819'][i]) == True) & (
                np.isnan(data['white8_1819'][i]) == True) & (np.isnan(data['white9_1819'][i]) == True) & (
                np.isnan(data['white10_1819'][i]) == True) & (np.isnan(data['white11_1819'][i]) == True) & (
                np.isnan(data['white12_1819'][i]) == True) & (np.isnan(data['white13_1819'][i]) == True) & (
                np.isnan(data['white14_1819'][i]) == True):
            data['White'][i] = np.nan
        if (np.isnan(data['grade0_total_1819'][i]) == True) & (np.isnan(data['grade1_total_1819'][i]) == True) & (
                np.isnan(data['grade2_total_1819'][i]) == True) & (np.isnan(data['grade3_total_1819'][i]) == True) & (
                np.isnan(data['grade4_total_1819'][i]) == True) & (np.isnan(data['grade5_total_1819'][i]) == True) & (
                np.isnan(data['grade6_total_1819'][i]) == True) & (np.isnan(data['grade7_total_1819'][i]) == True) & (
                np.isnan(data['grade8_total_1819'][i]) == True) & (np.isnan(data['grade9_total_1819'][i]) == True) & (
                np.isnan(data['grade10_total_1819'][i]) == True) & (np.isnan(data['grade11_total_1819'][i]) == True) & (
                np.isnan(data['grade12_total_1819'][i]) == True) & (np.isnan(data['grade13_total_1819'][i]) == True) & (
                np.isnan(data['grade14_total_1819'][i]) == True):
            data['Total_Enrollment'][i] = np.nan
        # remove the enrollments columns since total enrollment is required and calculated
    data = data.drop(enrollment_columns, axis=1)
    return data


def pct_subgroup(data):
    # Calculate the Percentage Subgroups for each School District
    data["American_Indian_pct"] = data["American_Indian"] * 100 / data["Total_Enrollment"]
    data["Asian_pct"] = data["Asian"] * 100 / data["Total_Enrollment"]
    data["Black_or_African_American_pct"] = data["Black_or_African_American"] * 100 / data["Total_Enrollment"]
    data["Hispanic_or_Latino_pct"] = data["Hispanic_or_Latino"] * 100 / data["Total_Enrollment"]
    data["Hawaiian_pct"] = data["Hawaiian"] * 100 / data["Total_Enrollment"]
    data["Not_Specified_pct"] = data["Not_Specified"] * 100 / data["Total_Enrollment"]
    data["Multi_Racial_pct"] = data["Multi_Racial"] * 100 / data["Total_Enrollment"]
    data["White_pct"] = data["White"] * 100 / data["Total_Enrollment"]
    return data
