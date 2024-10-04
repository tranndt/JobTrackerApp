#1: Initial Interface

#2:
- Cluster similar coordinates
- Job posting includes: posting_url, job_title, description, location, and date_created
    - Encountered some migration problems. Was able to overcome by adding default/blank fields
            ```
            company_name = models.CharField(max_length=255, blank="Untitled Company")
            job_title = models.CharField(max_length=255, blank="Untitled Job")  # New field
            ```
            ```
            python manage.py makemigrations tracker
            python manage.py migrate
            ```

#3:
- Import functionality
    - Can import title, company, location, description from LinkedIn url 
- Forwarded to a port

#4:
- Webdriver fetching capability. Can now fetch Indeed postings 
- Map in job view

#5:
- Base HTML
- Upload Document view
- All Documents view

#6.1:
- Site Refactoring (Tab names and URL)

#6.2: 
- Document name autofill

#6.3:
- Edit and Delete Document functionality

#6.4:
- Delete Job View
- Import from URL

#6.5:
- Delete Document entry on DB also delete locally

#7.0:
- Added Select/Upload Application (tbc)

#7.1:
- Moved Create Application to its own window
- Narrowed selections in resume, cover letter, other

#7.2:
- View, Edit application

#7.3:
- View application in view job

#7.4:
- Minor changes to view job