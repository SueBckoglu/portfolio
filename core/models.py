from django.db import models

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date"
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date"
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name",
        help_text='This is the variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description"
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Parameter"
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)



class Skill(AbstractModel):
    CATEGORY_CHOICES = (
        ('Frontend Development', 'Frontend Development'),
        ('Backend Development', 'Backend Development'),
        ('Programming & Scripting', 'Programming & Scripting'),
        ('Professional & Soft Skills', 'Professional & Soft Skills'),
    )

    order = models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name",
        help_text='This is the variable of the setting.'
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Category",
        default='Frontend Development'  # Varsayılan olarak "Frontend Development" seçeneği
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Company Name",
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Job Title",
    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Job Location",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End Date",
    )
    job_description = models.TextField(
        default='',
        blank=True,
        verbose_name="Job Description",
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('-start_date',)


class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="School Name",
    )
    department = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Department",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End Date",
    )
    courses = models.TextField(
        default='',
        blank=True,
        verbose_name="Courses",
    )

    def __str__(self):
        return f'Education: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ('-start_date',)


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    link = models.URLField(
        blank=True,
        default='',
        max_length=254,
        verbose_name="Link",
    )
    icon = models.CharField(
        blank=True,
        default='',
        max_length=254,
        verbose_name="Icon",
    )

    def __str__(self):
        return f'Social Media: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ('order',)


class Language(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    language_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Language",
    )
    level = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Level",
    )

    def __str__(self):
        return f'Language: {self.language_name}'

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Language'
        ordering = ('order',)


class Reference(AbstractModel):
    ref_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Reference Name",
        help_text='This is the variable of the setting.'
    )
    ref_company = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Reference Company"
    )
    ref_job = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Reference Job"
    )
    ref_email = models.EmailField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Reference Email",
    )
    ref_phone = models.CharField(
        default='',
        max_length=15,
        blank=True,
        verbose_name="Reference Phone",
    )
    ref_comment = models.TextField(
        default='',
        blank=True,
        verbose_name="Reference Comment",
    )

    def __str__(self):
        return f'Reference: {self.ref_name}'

    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'References'
        ordering = ('ref_name',)


class Project(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    project_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Project Name",
    )
    project_type = models.CharField(
        default='',
        max_length=100,
        blank=True,
        verbose_name="Project Type",
    )
    project_description = models.TextField(
        default='',
        blank=True,
        verbose_name="Project Description",
    )

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('order',)
