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

#4: