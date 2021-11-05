def check_result(res,dapAn):
    res_False=""
    res_no_check=""
    sum_Ture= 0
    for i in range(40):
        if res.get("{}".format(i))==dapAn[i]:
            sum_Ture=sum_Ture+1
        else:
            if res.get("{}".format(i))=="0":
                res_no_check = res_no_check+", {}".format(i+1)
            else:
                res_False = res_False+", {}:{}".format(i+1,dapAn[i])
    diem = 10*sum_Ture/40
    return " điểm: {}\n câu không làm: {}\n câu sai: {}".format(diem,res_no_check[1:],res_False[1:])



def get_result(key_mssv, key_class, key_test, res):
    result = ""
    name_list = {"1813150":"Hồ Quốc Nghĩa"}
    test_list_ML = {"12283":"meachine leaning",
                   "105":"AABACDBCDABCAADBSDABACDDBCAADABCABCCABAD"}
    test_list_AI = {"12598": "Trí tuệ nhân tạo",
                      "113": "ABACDDABADCCABCDAACDABAACDABDCCADDBACBCB"}
    if key_mssv in name_list:
        result = result+"tên sinh viên : {}".format(name_list.get(key_mssv))

    if key_class in test_list_AI:
        result = result+"\nmôn kiểm tra: {}".format(test_list_AI.get(key_class))
        if key_test in test_list_AI:
           result = result+"\n {}"/format(check_result(res,test_list_AI.get(key_test)))
    else:
        result = result+"\nmôn kiểm tra: {}".format(test_list_ML.get(key_class))
        if key_test in test_list_ML:
           result = result+"\n {}".format(check_result(res,test_list_ML.get(key_test)))

    return result
