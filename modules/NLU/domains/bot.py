import student_info
import student_info.get_data
import attendance.handle_query
import faculty.handle_query
import db.find_DB


def chat(query, intent):
    try:
        user = student_info.student_info.Student()

    except student_info.get_data.InvalidCredentials as e:
        print e.message
        exit(1)
    except student_info.get_data.LoginError as e:
        print e.message
        exit(1)

        # response = faculty.handle_query.process_query(query)
        # if response:
        #     return response
        #
        # response = attendance.handle_query.process_query(user, query)
        # if response:
        #     return response


    response = db.find_DB.get_response(query, intent, user)
    if response:
        return response

    return "can't get you"
