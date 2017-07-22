import attendance.student_info
import attendance.handle_query
import attendance
import faculty.handle_query
import db.find_DB


def chat(query):
    try:
        user = attendance.student_info.Student()

    except attendance.get_data.InvalidCredentials as e:
        print e.message
        exit(1)
    except attendance.get_data.LoginError as e:
        print e.message
        exit(1)

        # response = faculty.handle_query.process_query(query)
        # if response:
        #     return response
        #
        # response = attendance.handle_query.process_query(user, query)
        # if response:
        #     return response

    response = db.find_DB.get_response(query, user)
    if response:
        return response

    return "can't get you"
