import domain.user.repository as Repository

def create_user(data):
    if data['email'] is None or data['email'] == '':
        return {'msg': 'Email not valid', 'error': True}, 400
    
    if data['username'] is None or data['username'] == '':
        return {'msg': 'username not valid', 'error': True}, 400
        
    return Repository.create_user(data), 201