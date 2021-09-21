class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def create_password_hash(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, current_password):
        return check_password_hash(self.password, current_password)

    def save(self):
        self.create_password_hash(self.password)

        db.session.add(self)
        db.session.commit()

    def from_dict(self, data):
        for field in ['first_name', 'last_name', 'email', 'password']:
            if field in data:
                setattr(self, field, data[field])

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))