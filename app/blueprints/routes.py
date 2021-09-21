@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # look for the user in our database
        user = User.query.filter_by(email=email).first()
        # if the email and/or password don't match,
        if user is None or not user.check_password(password):
            # show an error messages
            flash('You typed in either an incorrect email or password', 'danger')
            # redirect to the login page
            return redirect(url_for('auth.login'))
        # otherwise
        # log the user in
        login_user(user)
        flash('You have logged in successfully!', 'info')
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is not None:
            flash('That user already exists. Please try another email address', 'warning')
            return redirect(url_for('auth.register'))
        if request.form.get('password') != request.form.get('confirm_password'):
            flash('Your password do not match.', 'danger')
            return redirect(url_for('auth.register'))
        u = User()
        u.from_dict(request.form)
        u.save()
        # print('It works!')
        flash('User has registered successfully', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out successfully', 'primary')
    return redirect(url_for('home'))

@app.route('/shop', method= ['GET', 'POST'])
def shop():
    if request.method == 'POST':
        user = pass

@app.route('/contact', method= ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # look for the user in our database
        user = User.query.filter_by(email=email).first()
        pass
        return redirect(url_for('home'))
    return render_template('login.html')