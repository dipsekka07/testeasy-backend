from examiner.resource.exams.exams_resource import exams, exams_id
RESOURCE_MAP = {
    '/exams': exams,
    '/exams/{exam_id}': exams_id
}


def invoke_resource(event_data):
    return RESOURCE_MAP.get(event_data.get('resource_path'))(event_data)
