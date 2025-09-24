import { useState } from "react";
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Switch } from "@/components/ui/switch";
import { FileUpload } from "@/components/ui/file-upload";
import { useAppContext } from "@/context/AppContext";
import { useToast } from "@/hooks/use-toast";
import { Plus, Edit, Trash2, Calendar, Clock, MapPin } from "lucide-react";
import type { Event } from "@/context/AppContext";

const validationSchema = Yup.object({
  title: Yup.string().required('Title is required'),
  description: Yup.string().required('Description is required'),
  date: Yup.string().required('Date is required'),
  time: Yup.string().required('Time is required'),
  location: Yup.string().required('Location is required'),
  image: Yup.string().required('Image is required'),
  registrationLink: Yup.string().url('Invalid URL').optional(),
  featured: Yup.boolean()
});

const AdminEvents = () => {
  const { state, dispatch } = useAppContext();
  const { toast } = useToast();
  const [isOpen, setIsOpen] = useState(false);
  const [editingEvent, setEditingEvent] = useState<Event | null>(null);

  const formik = useFormik({
    initialValues: {
      title: '',
      description: '',
      date: '',
      time: '',
      location: '',
      image: '',
      registrationLink: '',
      featured: false
    },
    validationSchema,
    onSubmit: (values, { resetForm }) => {
      if (editingEvent) {
        const updatedEvent: Event = {
          ...editingEvent,
          ...values
        };
        
        dispatch({ type: 'UPDATE_EVENT', payload: updatedEvent });
        toast({
          title: "Event Updated",
          description: "The event has been successfully updated."
        });
      } else {
        const newEvent: Event = {
          id: Date.now().toString(),
          ...values
        };
        
        dispatch({ type: 'ADD_EVENT', payload: newEvent });
        toast({
          title: "Event Added",
          description: "The new event has been successfully added."
        });
      }
      
      setIsOpen(false);
      resetForm();
      setEditingEvent(null);
    }
  });

  const handleEdit = (event: Event) => {
    setEditingEvent(event);
    formik.setValues({
      title: event.title,
      description: event.description,
      date: event.date,
      time: event.time,
      location: event.location,
      image: event.image,
      registrationLink: event.registrationLink || '',
      featured: event.featured
    });
    setIsOpen(true);
  };

  const handleDelete = (eventId: string) => {
    if (window.confirm('Are you sure you want to delete this event?')) {
      dispatch({ type: 'DELETE_EVENT', payload: eventId });
      toast({
        title: "Event Deleted",
        description: "The event has been successfully deleted.",
        variant: "destructive"
      });
    }
  };

  const openCreateDialog = () => {
    formik.resetForm();
    setEditingEvent(null);
    setIsOpen(true);
  };

  const formatDate = (dateStr: string) => {
    return new Date(dateStr).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  const formatTime = (timeStr: string) => {
    return new Date(`2000-01-01T${timeStr}`).toLocaleTimeString('en-US', {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true
    });
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold  text-gray-800 dark:text-foreground">Events Management</h2>
          <p className="text-muted-foreground">Manage church events and special gatherings</p>
        </div>

        <Dialog open={isOpen} onOpenChange={(open) => {
          setIsOpen(open);
          if (!open) {
            formik.resetForm();
            setEditingEvent(null);
          }
        }}>
          <DialogTrigger asChild>
            <Button variant="secondary" onClick={openCreateDialog}>
              <Plus  className="w-4 h-4 mr-2" />
              Add Event
            </Button>
          </DialogTrigger>
          <DialogContent title="TT" className=" max-h-[80vh] overflow-y-auto">
            <DialogHeader>
              <DialogTitle>
                {editingEvent ? 'Edit Event' : 'Add New Event'}
              </DialogTitle>
            </DialogHeader>
            <form onSubmit={formik.handleSubmit} className="space-y-4">
              <div>
                <Label htmlFor="title">Event Title</Label>
                <Input
                  id="title"
                  name="title"
                  value={formik.values.title}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  className="rounded-lg"
                />
                {formik.touched.title && formik.errors.title && (
                  <p className="text-sm text-red-500">{formik.errors.title}</p>
                )}
              </div>
              
              <div>
                <Label htmlFor="description">Description</Label>
                <Textarea
                  id="description"
                  name="description"
                  value={formik.values.description}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                />
                {formik.touched.description && formik.errors.description && (
                  <p className="text-sm text-red-500">{formik.errors.description}</p>
                )}
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <Label htmlFor="date">Date</Label>
                  <Input
                    id="date"
                    name="date"
                    type="date"
                    value={formik.values.date}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                  />
                  {formik.touched.date && formik.errors.date && (
                    <p className="text-sm text-red-500">{formik.errors.date}</p>
                  )}
                </div>
                <div>
                  <Label htmlFor="time">Time</Label>
                  <Input
                    id="time"
                    name="time"
                    type="time"
                    value={formik.values.time}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                  />
                  {formik.touched.time && formik.errors.time && (
                    <p className="text-sm text-red-500">{formik.errors.time}</p>
                  )}
                </div>
              </div>

              <div>
                <Label htmlFor="location">Location</Label>
                <Input
                  id="location"
                  name="location"
                  value={formik.values.location}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                />
                {formik.touched.location && formik.errors.location && (
                  <p className="text-sm text-red-500">{formik.errors.location}</p>
                )}
              </div>

              <FileUpload
                id="image"
                name="image"
                label="Event Image"
                value={formik.values.image}
                onChange={(value) => formik.setFieldValue('image', value)}
                onBlur={() => formik.setFieldTouched('image')}
                error={formik.touched.image && formik.errors.image ? formik.errors.image : undefined}
              />

              <div>
                <Label htmlFor="registrationLink">Registration Link (Optional)</Label>
                <Input
                  id="registrationLink"
                  name="registrationLink"
                  type="url"
                  value={formik.values.registrationLink}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                />
                {formik.touched.registrationLink && formik.errors.registrationLink && (
                  <p className="text-sm text-red-500">{formik.errors.registrationLink}</p>
                )}
              </div>

              <div className="flex items-center space-x-2">
                <Switch
                  id="featured"
                  checked={formik.values.featured}
                  onCheckedChange={(checked) => formik.setFieldValue('featured', checked)}
                />
                <Label htmlFor="featured">Featured Event</Label>
              </div>

              <div className="flex gap-2 pt-4">
                <Button type="submit" variant="secondary" className="flex-1" disabled={formik.isSubmitting}>
                  {editingEvent ? 'Update Event' : 'Add Event'}
                </Button>
                <Button 
                  type="button" 
                  variant="outline" 
                  onClick={() => setIsOpen(false)}
                  className={"hover:bg-gray-200"}
                >
                  Cancel
                </Button>
              </div>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {state.events.map((event) => (
          <Card key={event.id} className="overflow-hidden relative">
            <div className="relative">
              <img 
                src={event.image} 
                alt={event.title}
                className="w-full h-32 object-cover rounded-t-lg"
              />
              {event.featured && (
                <div className="absolute top-2 left-2 bg-slate-800 text-primary-foreground text-xs px-2 py-1 rounded">
                  Featured
                </div>
              )}
            </div>
            
            <CardHeader className="pb-2">
              <CardTitle className="text-lg text-gray-50 ">{event.title}</CardTitle>
            </CardHeader>
            
            <CardContent className="space-y-3">
              <p className="text-sm text-slate-200 line-clamp-2">
                {event.description}
              </p>
              
              <div className="space-y-1 text-xs text-slate-300">
                <div className="flex items-center">
                  <Calendar className="w-3 h-3 mr-1" />
                  {formatDate(event.date)}
                </div>
                <div className="flex items-center">
                  <Clock className="w-3 h-3 mr-1" />
                  {formatTime(event.time)}
                </div>
                <div className="flex items-center">
                  <MapPin className="w-3 h-3 mr-1" />
                  {event.location}
                </div>
              </div>

              <div className="flex gap-2 pt-2">
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => handleEdit(event)}
                  className="flex-1 rounded text-gray-200"
                >
                  <Edit className="w-3 h-3 mr-1" />
                  Edit
                </Button>
                <Button
                  variant="secondary"
                  size="sm"
                  className="bg-red-500 text-white rounded hover:bg-red-300"
                  onClick={() => handleDelete(event.id)}
                >
                  <Trash2 className="w-3 h-3" />
                </Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {state.events.length === 0 && (
        <Card className="text-center py-12">
          <CardContent>
            <Calendar className="w-12 h-12 text-muted-foreground mx-auto mb-4" />
            <h3 className="text-lg font-medium text-foreground mb-2">No Events Yet</h3>
            <p className="text-muted-foreground mb-4">
              Start by adding your first church event.
            </p>
            <Button onClick={openCreateDialog}>
              <Plus className="w-4 h-4 mr-2" />
              Add Your First Event
            </Button>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default AdminEvents;