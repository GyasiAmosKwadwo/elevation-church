from django.db import models
from django.conf import settings
import uuid
from datetime import datetime

class Sermon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, help_text="Enter the title of the sermon")
    description = models.CharField(max_length=700, help_text="Enter a brief description of the sermon")
    video_link = models.URLField(default="https://www.youtube.com/watch?v=sjkrrmBnpGE&t=11s", help_text="Enter the video link of the sermon")
    preacher = models.CharField(max_length=100, default="Pastor Obed Agyiri", help_text="Enter the name of the preacher")
    podcast_link = models.URLField(blank=True, help_text="Enter the podcast link of the sermon")
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, null=True, related_name='sermon', help_text="Enter any additional resources for the sermon")
    series = models.ForeignKey('Series', on_delete=models.CASCADE, null=True, related_name='sermon_series', help_text="Select the series this sermon belongs to")
    likes = models.IntegerField(default=0, help_text="Number of likes for this reflection")
    comments = models.TextField(blank=True, help_text="Comments on the reflection")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, help_text="Enter the name of the resource")
    purchase_link = models.URLField(help_text="Enter the purchase link of the resource")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Enter the price of the resource")

    def __str__(self):
        return self.name

class Series(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, help_text="Enter the title of the series")
    description = models.CharField(max_length=700, help_text="Enter a brief description of the series")
    available_sermons = models.ManyToManyField(Sermon, related_name='series_sermons', blank=True, help_text="Select sermons that belong to this series")
    image = models.ImageField(upload_to='series_images/', max_length=500, default='https://www.freepik.com/free-photo/woman-praying-her-loved-ones_12690245.htm#fromView=search&page=1&position=49&uuid=b8c3c77b-8227-4daf-b533-f58011aa9874&query=bible+studies', help_text="Upload an image for the series")
    likes = models.IntegerField(default=0, help_text="Number of likes for this Series")
    thoughts=models.ManyToManyField('Reflection', related_name='series_thoughts', blank=True, help_text="Add thoughts on this series")
    date = models.DateTimeField(auto_now_add=True, help_text="Date the series was created")

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-date']

    def __str__(self):
        return self.title

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default="Congregational meeting", max_length=200, help_text="Enter the name of the event")
    description = models.CharField(max_length=700, help_text="Enter a brief description of the event")
    flyer = models.ImageField(upload_to='event_flyers/', max_length=500, default='https://www.freepik.com/free-photo/empty-christian-church-building_144641216.htm#fromView=search&page=1&position=1&uuid=7df8b822-77d5-4328-b319-154627617e08&query=church', help_text="Upload a flyer for the event")    
    location = models.CharField(max_length=300, help_text="Enter the location of the event")
    date= models.DateField(help_text="Enter the start date of the event")
    days = models.IntegerField(default=1, help_text="Number of days the event lasts")
    start_time = models.TimeField(null=True, blank=True, help_text="Enter the start time of the event")
    end_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Devotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, help_text="Enter the title of the devotional")
    Bible_verse = models.JSONField(default=dict, help_text="Enter the Bible verse as a JSON object with 'reference' and 'verse_content'")
    content = models.TextField(help_text="Enter the content of the devotional")
    thumbnail = models.ImageField(upload_to='devotion_thumbnails/', max_length=500, null = True, help_text="Upload a thumbnail for the devotional")
    #reflection = models.ManyToManyField('Reflection', related_name='devotion_reflections', blank=True, help_text="Add reflections for this devotional")
    date = models.DateTimeField(default=datetime.now, help_text="Date the devotional was created")
    

    def __str__(self):
        return self.title
    

class Reflection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, help_text="Enter your name here")
    content = models.TextField(help_text="Enter the content of the reflection")
    likes = models.IntegerField(default=0, help_text="Number of likes for this reflection")
    comments = models.TextField(blank=True, help_text="Comments on the reflection")
    devotion = models.ForeignKey(
        'Devotion',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='reflections',
        help_text="Select the devotion this reflection belongs to"
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:10] + '...' if len(self.content) > 10 else self.content

    
class Prayer_request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, help_text="Enter your name here")
    subject = models.TextField(help_text="Enter the content of your prayer request")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, help_text="Enter the title of the announcement")
    content = models.TextField(help_text="Enter the content of the announcement")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
STATUS_CHOICES = [
    ('live', 'Live'),
    ('upcoming', 'Upcoming'),
    ('past', 'Past'),
]
    
class Live_stream(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, help_text="Enter the title of the live stream")
    description = models.CharField(max_length=700, help_text="Enter a brief description of the live stream")
    stream_link = models.URLField(default="https://www.youtube.com/watch?v=sjkrrmBnpGE&t=11s", help_text="Enter the stream link of the live stream")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming', help_text="Status of the live stream")
    reactions = models.IntegerField(default=0, help_text="Number of reactions for this live stream")
    comments = models.TextField(blank=True, help_text="Comments on the live stream")
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title
    

class Gallery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, help_text="Enter the title of the gallery")
    description = models.CharField(max_length=700, help_text="Enter a brief description of the gallery")
    venue = models.CharField(max_length=300, help_text="Enter the venue where the images were taken", blank=True)
    likes = models.IntegerField(default=0, help_text="Number of likes for this gallery")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gallery = models.ForeignKey('Gallery', null=True, blank=True, on_delete=models.CASCADE, related_name='images', help_text="Select the gallery this image belongs to")
    title = models.CharField(max_length=200, help_text="Enter the title of the gallery image")
    image = models.ImageField(upload_to='gallery_images/', max_length=500, help_text="Upload the gallery image")
    description = models.CharField(max_length=700, help_text="Enter a brief description of the gallery image")
    venue = models.CharField(max_length=300, help_text="Enter the venue where the image was taken", blank=True)
    likes = models.IntegerField(default=0, help_text="Number of likes for this gallery image")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContributionChannel(models.Model):
    CHANNEL_CHOICES = [
        ('momo', 'MOMO'),
        ('bank', 'BANK'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, help_text="Display name for the receiving account")
    channel_type = models.CharField(max_length=10, choices=CHANNEL_CHOICES, help_text="Contribution channel type")
    account_name = models.CharField(max_length=200, help_text="Account holder name")
    account_number = models.CharField(max_length=120, help_text="MOMO number or bank account number")
    bank_name = models.CharField(max_length=150, blank=True, help_text="Bank name (for bank channels)")
    branch = models.CharField(max_length=150, blank=True, help_text="Bank branch (optional)")
    network = models.CharField(max_length=100, blank=True, help_text="MOMO network (for MOMO channels)")
    currency = models.CharField(max_length=10, default='GHS', help_text="Currency code, e.g. GHS")
    instructions = models.TextField(blank=True, help_text="Optional guidance shown to contributors")
    is_active = models.BooleanField(default=True, help_text="Whether this receiving account is currently active")
    display_order = models.PositiveIntegerField(default=0, help_text="Sort order for displaying channels")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} ({self.channel_type.upper()})"


class ContributionIntent(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]
    PURPOSE_CHOICES = [
        ('tithe', 'Tithe'),
        ('offering', 'Offering'),
        ('project', 'Project'),
        ('donation', 'Donation'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    channel = models.ForeignKey(ContributionChannel, on_delete=models.PROTECT, related_name='intents')
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount contributor sent")
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default='donation')
    donor_name = models.CharField(max_length=200, blank=True, help_text="Contributor name (optional)")
    donor_phone = models.CharField(max_length=30, blank=True, help_text="Contributor phone (optional)")
    reference = models.CharField(max_length=120, blank=True, help_text="Bank/MOMO transfer reference")
    proof_url = models.URLField(blank=True, help_text="Optional proof screenshot URL")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_note = models.TextField(blank=True, help_text="Internal note by admin/staff")
    confirmed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='confirmed_contribution_intents'
    )
    confirmed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.channel.name} - {self.amount} ({self.status})"


class Reel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    caption = models.TextField(blank=True)
    video_url = models.URLField(help_text="Publicly accessible reel video URL")
    thumbnail_url = models.URLField(blank=True, help_text="Optional reel thumbnail image URL")
    category = models.CharField(max_length=100, blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_reels'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title
