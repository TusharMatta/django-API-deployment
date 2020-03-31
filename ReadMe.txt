Django API project

*************USAGE***********

All response will have the form:

***json
{
    
}
***

Subsequent response definitions will only detail the response value of the 'data fields'

***List of all the users***

'GET /final'

**Response**
- '200 OK' on success
*json
{
    'ok': True
    'members' : 'Details of members in json format'
    
}
*

**
***

***GET, POST, UPDATE, DELETE users***

'/users/'

**Response**
- '200 OK' on get success
- '200 created' on post success
- '204 not found' on delete success

*json
{
        "realname": "",
        "continent": "",
        "country": "",
        "activity_periods": [
            {
                "start_time": "",
                "end_time": ""
            }
          }
 }
 *
 **
 ***
 
 
 ***Detail of all specific user***
 
 '/users/id/'
 
 **Response**
- '200 OK' on success
- 'not found' if user not exist

*json
{
        "realname": "",
        "continent": "",
        "country": "",
        "activity_periods": [
            {
                "start_time": "",
                "end_time": ""
            }
          }
 }
 *
 **
 ***

