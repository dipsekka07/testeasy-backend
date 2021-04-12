from examiner.resource.exams.exam_utils import get_exam_detail_by_id, get_all_exams, create_new_exam


def exams(event_data):  
    http_method = event_data.get('resource_method')
    if(http_method == 'GET'):
        return get_all_exams(event_data)
    if(http_method == 'POST'):
        return create_new_exam(event_data)


def exams_id(event_data):
    http_method = event_data.get('resource_method')
    if(http_method == 'GET'):
        return get_exam_detail_by_id(event_data)






