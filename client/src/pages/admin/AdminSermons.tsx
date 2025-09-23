import { useState } from "react";
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Badge } from "@/components/ui/badge";
import { FileUpload } from "@/components/ui/file-upload";
import { useAppContext, Sermon } from "@/context/AppContext";
import { Plus, Edit, Trash2, Calendar, Play } from "lucide-react";
import { toast } from "@/hooks/use-toast";
import {getYouTubeVideoId} from "@/utili/utili";

const validationSchema = Yup.object({
  title: Yup.string().required('Title is required'),
  description: Yup.string().required('Description is required'),
  videoUrl: Yup.string().url('Invalid URL').required('Video URL is required'),
  podcastUrl: Yup.string().url('Invalid URL').optional(),
  preacher: Yup.string().required('Preacher is required'),
  date: Yup.string().required('Date is required'),
  series: Yup.string().optional(),
  tags: Yup.string().optional(),
});

const AdminSermons = () => {
  const { state, dispatch } = useAppContext();
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingSermon, setEditingSermon] = useState<Sermon | null>(null);

  const formik = useFormik({
    initialValues: {
      title: "",
      description: "",
      videoUrl: "",
      podcastUrl: "",
      preacher: "",
      date: "",
      series: "",
      tags: "",
    },
    validationSchema,
    onSubmit: (values, { resetForm }) => {
      const tags = values.tags.split(",").map(tag => tag.trim()).filter(Boolean);
      
      const sermonData: Sermon = {
        id: editingSermon?.id || Date.now().toString(),
        title: values.title,
        description: values.description,
        videoUrl: values.videoUrl,
        podcastUrl: values.podcastUrl || undefined,
        preacher: values.preacher,
        date: values.date,
        series: values.series || undefined,
        tags
      };

      if (editingSermon) {
        dispatch({ type: 'UPDATE_SERMON', payload: sermonData });
        toast({
          title: "Sermon updated",
          description: "The sermon has been successfully updated.",
        });
      } else {
        dispatch({ type: 'ADD_SERMON', payload: sermonData });
        toast({
          title: "Sermon created",
          description: "The new sermon has been successfully created.",
        });
      }

      setIsDialogOpen(false);
      resetForm();
      setEditingSermon(null);
    }
  });

  const openCreateDialog = () => {
    formik.resetForm();
    setEditingSermon(null);
    setIsDialogOpen(true);
  };

  const openEditDialog = (sermon: Sermon) => {
    formik.setValues({
      title: sermon.title,
      description: sermon.description,
      videoUrl: sermon.videoUrl,
      podcastUrl: sermon.podcastUrl || "",
      preacher: sermon.preacher,
      date: sermon.date,
      series: sermon.series || "",
      tags: sermon.tags.join(", "),
    });
    setEditingSermon(sermon);
    setIsDialogOpen(true);
  };

  const handleDelete = (id: string) => {
    if (confirm("Are you sure you want to delete this sermon?")) {
      dispatch({ type: 'DELETE_SERMON', payload: id });
      toast({
        title: "Sermon deleted",
        description: "The sermon has been successfully deleted.",
      });
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-800 dark:text-foreground">Manage Sermons</h2>
          <p className="text-muted-foreground">Create, edit, and organize your sermon library</p>
        </div>
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogTrigger asChild>
            <Button  variant="secondary" className={"rounded dark:bg-gray-700"} onClick={openCreateDialog}>
              <Plus className="w-4 h-4 mr-2" />
              Add Sermon
            </Button>
          </DialogTrigger>
          <DialogContent className="sm:max-w-lg rounded-lg max-h-[80vh] overflow-y-auto">
            <DialogHeader>
              <DialogTitle>
                {editingSermon ? "Edit Sermon" : "Add New Sermon"}
              </DialogTitle>
              <DialogDescription>
                {editingSermon 
                  ? "Update the sermon information below." 
                  : "Fill in the details to create a new sermon."}
              </DialogDescription>
            </DialogHeader>
            <form onSubmit={formik.handleSubmit} className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="title">Title</Label>
                  <Input
                    id="title"
                    name="title"
                    value={formik.values.title}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                  />
                  {formik.touched.title && formik.errors.title && (
                    <p className="text-sm text-red-400">{formik.errors.title}</p>
                  )}
                </div>
                <div className="space-y-2">
                  <Label htmlFor="preacher">Preacher</Label>
                  <Input
                    id="preacher"
                    name="preacher"
                    value={formik.values.preacher}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                  />
                  {formik.touched.preacher && formik.errors.preacher && (
                    <p className="text-sm text-red-400">{formik.errors.preacher}</p>
                  )}
                </div>
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="description">Description</Label>
                <Textarea
                  id="description"
                  name="description"
                  value={formik.values.description}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                />
                {formik.touched.description && formik.errors.description && (
                  <p className="text-sm text-red-400">{formik.errors.description}</p>
                )}
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="videoUrl">Video URL</Label>
                  <Input
                    id="videoUrl"
                    name="videoUrl"
                    type="url"
                    value={formik.values.videoUrl}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                  />
                  {formik.touched.videoUrl && formik.errors.videoUrl && (
                    <p className="text-sm text-red-400">{formik.errors.videoUrl}</p>
                  )}
                </div>
                <div className="space-y-2">
                  <Label htmlFor="podcastUrl">Podcast URL (Optional)</Label>
                  <Input
                    id="podcastUrl"
                    name="podcastUrl"
                    type="url"
                    value={formik.values.podcastUrl}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                  />
                  {formik.touched.podcastUrl && formik.errors.podcastUrl && (
                    <p className="text-sm text-red-400">{formik.errors.podcastUrl}</p>
                  )}
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-2">
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
                    <p className="text-sm text-red-400">{formik.errors.date}</p>
                  )}
                </div>
                <div className="space-y-2">
                  <Label htmlFor="series">Series (Optional)</Label>
                  <Select value={formik.values.series} onValueChange={(value) => formik.setFieldValue('series', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select a series" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem  value="gdg">No Series</SelectItem>
                      {state.series.map((series) => (
                        <SelectItem key={series.id} value={series.title}>
                          {series.title}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="tags">Tags (comma-separated)</Label>
                <Input
                  id="tags"
                  name="tags"
                  value={formik.values.tags}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  placeholder="faith, prayer, worship"
                />
              </div>

              <div className="flex justify-end space-x-2">
                <Button type="button" variant="outline" onClick={() => setIsDialogOpen(false)}>
                  Cancel
                </Button>
                <Button type="submit" variant="secondary" className="rounded bg-blue-900 text-white dark:bg-gray-700" disabled={formik.isSubmitting}>
                  {editingSermon ? "Update" : "Create"} Sermon
                </Button>
              </div>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      {/* Sermons List */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {state.sermons.map((sermon) => (
          <Card key={sermon.id} className="h-[430px] group overflow-hidden shadow-lg">
            <CardHeader className="p-0">
              <div className="aspect-video bg-muted rounded-t-lg flex items-center justify-center overflow-hidden">
                {sermon.videoUrl ? (
                  <img
                      src={`https://i.ytimg.com/vi/${getYouTubeVideoId(sermon.videoUrl)}/hqdefault.jpg`}
                      alt={sermon.title}
                      className="w-full h-full object-cover"
                  />
                ) : (
                  <Play className="w-8 h-8 text-muted-foreground" />
                )}
              </div>
            </CardHeader>
            <CardContent className="p-4">
              <div className="space-y-3">
                {sermon.series && (
                  <Badge variant="secondary" className="text-xs bg-gray-200">
                    {sermon.series}
                  </Badge>
                )}
                <CardTitle className="text-lg text-gray-300 line-clamp-2">{sermon.title}</CardTitle>
                <CardDescription className="line-clamp-2">
                  {sermon.description}
                </CardDescription>
                <div className="flex items-center justify-between text-sm text-gray-300 darK:text-muted-foreground">
                  <span>{sermon.preacher}</span>
                  <span className="flex items-center">
                    <Calendar className="w-3 h-3 mr-1" />
                    {new Date(sermon.date).toLocaleDateString()}
                  </span>
                </div>
                <div className="pt-2 flex justify-end space-x-2">
                  <Button
                    variant="outline"
                    size="sm"
                    className="rounded text-gray-200"
                    onClick={() => openEditDialog(sermon)}
                  >
                    <Edit className="w-3 h-3 mr-1" />
                    Edit
                  </Button>
                  <Button
                    variant="secondary"
                    size="sm"
                    onClick={() => handleDelete(sermon.id)}
                    className="bg-gray-100 hover:bg-red-500 text-red-500 hover:text-gray-50 rounded"
                  >
                    <Trash2 className="w-3 h-3 mr-1" />
                    Delete
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {state.sermons.length === 0 && (
        <Card>
          <CardContent className="p-12 text-center">
            <Play className="w-16 h-16 text-muted-foreground mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-foreground mb-2">No sermons yet</h3>
            <p className="text-muted-foreground mb-4">
              Start building your sermon library by adding your first sermon.
            </p>
            <Button onClick={openCreateDialog}>
              <Plus className="w-4 h-4 mr-2" />
              Add Your First Sermon
            </Button>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default AdminSermons;