import json
import boto3
from ez2erp_engine.db import Ez2DBManager
from endpoints import auth, user


def lambda_handler(event, context):
    # TODO: Move keys to enviroment variable
    session = boto3.Session(
        aws_access_key_id="AKIA47CRWL5IINEGSZNO",
        aws_secret_access_key="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",
        region_name='ap-southeast-1'
    )
    Ez2DBManager.connect_db(session)

    # Request parameters
    endpoint = event.get('endpoint')
    http_method = event['requestContext']['http']['method']
    
    match endpoint:
        case "login":
            result = auth.login(event)
            message = ""
            return result
        case "users":
            if http_method == 'GET':
                pass
            elif http_method == 'POST':
                result = user.create_user(event)
            message = "User created successfully!"

        case "orders":
            pass
        case "payments":
            pass
        case default:
            message = "Endpoint is not available"
            return {
                'status': 'error',
                'message': message
            }
    
    return {
        'status': 'success',
        'message': message
    }

if __name__ == '__main__':
    event = {
        'endpoint': 'login',
    }

    create_user_event = {
        'endpoint': 'users',
        'requestContext': {'http': {'method': 'POST'}},
        'email': 'rmontemayor0101@gmail.com',
        'phone_no': '09288657242',
        'fname': 'Rob',
        'lname': 'Mon',
        'mname': '',
        'password': 'adminpassword'
    }
    context = {}
    lambda_handler(create_user_event, context)
