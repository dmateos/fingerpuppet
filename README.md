## Django skeleton application
- Common stuff i normall need to setup at the start of a project
- Saves about an hour of fucking around
- Will add more stuff overtime as i extract it from projects i do

### Serverless/Elastic Beanstalk ready 
- settings.py can use sqlite/mysql based on env var switch
- os.environ.get() used for db/auth etc for slipping in serverless/eb settings
- Zappa settings for lambda deployments
- Boiled down requirements.txt for venvs

### Bootstrap 4 setup
- Some basic templates
- Navbar login/logout/logic
- Lib installed/style setup

### Some user management 
- Login
- Register
- Linked account model with signal hookup
- Index/Home/Dashboard logged in/out logic

### Lib dir 
- Use for domain logic

### Git pre-commit workflow
- Black
- Flake8

### Misc
- Example views/model
- AppConfiguration model for storing global config
- Pytest setup with example structure/tests
- Coverage.py integration with pytest setup

