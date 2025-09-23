import { useState } from "react";
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Badge } from "@/components/ui/badge";
import { FileUpload } from "@/components/ui/file-upload";
import { useAppContext, Series } from "@/context/AppContext";
import { Plus, Edit, Trash2, Book } from "lucide-react";
import { toast } from "@/hooks/use-toast";

const validationSchema = Yup.object({
  title: Yup.string().required('Title is required'),
  description: Yup.string().required('Description is required'),
  thumbnail: Yup.string().required('Thumbnail is required')
});

const AdminSeries = () => {
  const { state, dispatch } = useAppContext();
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [editingSeries, setEditingSeries] = useState<Series | null>(null);

  const formik = useFormik({
    initialValues: {
      title: "",
      description: "",
      thumbnail: ""
    },
    validationSchema,
    onSubmit: (values, { resetForm }) => {
      const seriesData: Series = {
        id: editingSeries?.id || Date.now().toString(),
        title: values.title,
        description: values.description,
        sermons: editingSeries?.sermons || [],
        thumbnail: values.thumbnail
      };

      if (editingSeries) {
        dispatch({ type: 'UPDATE_SERIES', payload: seriesData });
        toast({
          title: "Series updated",
          description: "The series has been successfully updated.",
        });
      } else {
        dispatch({ type: 'ADD_SERIES', payload: seriesData });
        toast({
          title: "Series created",
          description: "The new series has been successfully created.",
        });
      }

      setIsDialogOpen(false);
      resetForm();
      setEditingSeries(null);
    }
  });

  const openCreateDialog = () => {
    formik.resetForm();
    setEditingSeries(null);
    setIsDialogOpen(true);
  };

  const openEditDialog = (series: Series) => {
    formik.setValues({
      title: series.title,
      description: series.description,
      thumbnail: series.thumbnail
    });
    setEditingSeries(series);
    setIsDialogOpen(true);
  };

  const handleDelete = (id: string) => {
    if (confirm("Are you sure you want to delete this series? This will not delete the sermons.")) {
      dispatch({ type: 'DELETE_SERIES', payload: id });
      toast({
        title: "Series deleted",
        description: "The series has been successfully deleted.",
      });
    }
  };

  const getSermonCount = (seriesTitle: string) => {
    return state.sermons.filter(sermon => sermon.series === seriesTitle).length;
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-800 dark:text-foreground">Manage Series</h2>
          <p className="text-muted-foreground">Create and organize sermon series</p>
        </div>
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogTrigger asChild>
            <Button variant="secondary" className="rounded" onClick={openCreateDialog}>
              <Plus className="w-4 h-4 mr-2" />
              Add Series
            </Button>
          </DialogTrigger>
          <DialogContent className="sm:max-w-[500px]">
            <DialogHeader>
              <DialogTitle>
                {editingSeries ? "Edit Series" : "Add New Series"}
              </DialogTitle>
              <DialogDescription>
                {editingSeries 
                  ? "Update the series information below." 
                  : "Fill in the details to create a new sermon series."}
              </DialogDescription>
            </DialogHeader>
            <form onSubmit={formik.handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="title">Series Title</Label>
                <Input
                  id="title"
                  name="title"
                  value={formik.values.title}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  placeholder="e.g., Ephesus 8, Heart Training"
                />
                {formik.touched.title && formik.errors.title && (
                  <p className="text-sm text-red-400">{formik.errors.title}</p>
                )}
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="description">Description</Label>
                <Textarea
                  id="description"
                  name="description"
                  value={formik.values.description}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  placeholder="Describe what this series is about..."
                  className="min-h-[100px]"
                />
                {formik.touched.description && formik.errors.description && (
                  <p className="text-sm text-red-400">{formik.errors.description}</p>
                )}
              </div>

              <FileUpload
                id="thumbnail"
                name="thumbnail"
                label="Series Thumbnail"
                value={formik.values.thumbnail}
                onChange={(value) => formik.setFieldValue('thumbnail', value)}
                onBlur={() => formik.setFieldTouched('thumbnail')}
                error={formik.touched.thumbnail && formik.errors.thumbnail ? formik.errors.thumbnail : undefined}
              />

              <div className="flex justify-end space-x-2">
                <Button type="button" variant="outline" onClick={() => setIsDialogOpen(false)}>
                  Cancel
                </Button>
                <Button type="submit" variant="secondary" className="rounded bg-blue-900 text-white dark:bg-gray-700" disabled={formik.isSubmitting}>
                  {editingSeries ? "Update" : "Create"} Series
                </Button>
              </div>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      {/* Series List */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {state.series.map((series) => {
          const sermonCount = getSermonCount(series.title);
          
          return (
            <Card key={series.id} className="overflow-hidden group">
              <CardHeader className="p-0">
                <div className="aspect-video rounded-t-lg flex items-center justify-center overflow-hidden">
                  {series.thumbnail ? (
                    <img src={series.thumbnail} alt={series.title} className="w-full h-full object-cover" />
                  ) : (
                    <div className="bg-gradient-to-br from-primary/10 to-accent/10 w-full h-full flex items-center justify-center">
                      <Book className="w-12 h-12 text-primary" />
                    </div>
                  )}
                </div>
              </CardHeader>
              <CardContent className="p-4">
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <Badge variant="secondary" className="text-xs bg-gray-200">
                      {sermonCount} sermon{sermonCount !== 1 ? 's' : ''}
                    </Badge>
                  </div>
                  
                  <CardTitle className="text-lg text-gray-300 line-clamp-2">{series.title}</CardTitle>
                  <CardDescription className="line-clamp-3">
                    {series.description}
                  </CardDescription>
                  
                  <div className="flex justify-end space-x-2">
                    <Button
                      variant="outline"
                      size="sm"
                      className="rounded text-gray-200"
                      onClick={() => openEditDialog(series)}
                    >
                      <Edit className="w-3 h-3 mr-1" />
                      Edit
                    </Button>
                    <Button
                      variant="secondary"
                      size="sm"
                      onClick={() => handleDelete(series.id)}
                      className="bg-gray-100 hover:bg-red-500 text-red-500 hover:text-gray-50 rounded"
                    >
                      <Trash2 className="w-3 h-3 mr-1" />
                      Delete
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          );
        })}
      </div>

      {state.series.length === 0 && (
        <Card>
          <CardContent className="p-12 text-center">
            <Book className="w-16 h-16 text-muted-foreground mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-foreground mb-2">No series yet</h3>
            <p className="text-muted-foreground mb-4">
              Start organizing your sermons by creating your first series.
            </p>
            <Button onClick={openCreateDialog}>
              <Plus className="w-4 h-4 mr-2" />
              Create Your First Series
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Help Section */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg">About Series</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <p className="text-sm text-muted-foreground">
            Sermon series help organize related messages together. When you create a series, you can assign sermons to it when adding or editing them.
          </p>
          <div className="space-y-2">
            <h4 className="text-sm font-semibold text-foreground">Tips:</h4>
            <ul className="text-sm text-muted-foreground space-y-1 ml-4">
              <li>• Create series for related messages or Bible book studies</li>
              <li>• Use descriptive titles that help visitors understand the theme</li>
              <li>• Write clear descriptions that explain what the series covers</li>
              <li>• Sermons are automatically added to series when you assign them</li>
            </ul>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default AdminSeries;