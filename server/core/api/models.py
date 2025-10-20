from django.db import models
import uuid

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
    image = models.ImageField(upload_to='series_images/', default='series_images/default_profile.jpg', help_text="Upload an image for the series")
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
    flyer = models.ImageField(upload_to='event_flyers/', default='event_flyers/default_profile.jpg', help_text="Upload a flyer for the event")    
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
    title = models.CharField(max_length=200, help_text="Enter the title of the devotional")
    Bible_verse = models.JSONField(default=dict, help_text="Enter the Bible verse as a JSON object with 'reference' and 'verse_content'")
    content = models.TextField(help_text="Enter the content of the devotional")
    thumbnail = models.ImageField(upload_to='devotion_thumbnails/', default='devotion_thumbnails/default_devotion_thumbnail.jpg', help_text="Upload a thumbnail for the devotional")
    reflection = models.ManyToManyField('Reflection', related_name='devotion_reflections', blank=True, help_text="Add reflections for this devotional")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Reflection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, help_text="Enter your name here")
    content = models.TextField(help_text="Enter the content of the reflection")
    likes = models.IntegerField(default=0, help_text="Number of likes for this reflection")
    comments = models.TextField(blank=True, help_text="Comments on the reflection")
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
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

