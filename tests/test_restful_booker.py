import requests

bokingID = None

# auth - no creds
def test_bad_creds(baseURL):
    response = requests.post(baseURL + 'auth')
    assert response.status_code == 200
    assert response.text == '{"reason":"Bad credentials"}'

#auth - valid creds
def test_valid_creds(baseURL, creds):
    response = requests.post(baseURL + 'auth', json=creds)
    assert response.status_code == 200
    assert 'token' in response.text
    
# create booking
def test_post_booking(baseURL, new_booking):
    global bookingId
    response = requests.post(baseURL + 'booking', json=new_booking)
    assert 'bookingid' in response.text
    assert response.status_code == 200
    bookingId = response.json()['bookingid']

# update booking
def test_put_booking(baseURL, updated_booking):
    global bookingId
    headers = {'Content-Type': 'application/json', 'Authorization' : 'Basic YWRtaW46cGFzc3dvcmQxMjM='}
    response = requests.put(baseURL + 'booking/' + f'{bookingId}' , json=updated_booking, headers=headers)
    assert response.status_code == 200

# get updated booking
def test_get_booking(baseURL):
    global bookingId
    response = requests.get(baseURL + 'booking/' + f'{bookingId}')
    data = response.json()
    assert data['additionalneeds'] == "no Breakfast"
    assert data['bookingdates']['checkin'] == "2019-01-01"