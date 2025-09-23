import { useParams, Link, useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { useAppContext } from "@/context/AppContext";
import { Play, Calendar, ArrowLeft, Book } from "lucide-react";
import {getYouTubeVideoId} from "@/utili/utili";

const SeriesDetail = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { state } = useAppContext();
  
  const series = state.series.find(s => s.id === id);
  
  if (!series) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-foreground mb-4">Series Not Found</h1>
          <p className="text-muted-foreground mb-6">The series you're looking for doesn't exist.</p>
          <Button variant={"secondary"} onClick={() => navigate('/series')}>
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Series
          </Button>
        </div>
      </div>
    );
  }

  const seriesSermons = state.sermons
    .filter(sermon => series.sermons.includes(sermon.id))
    .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime());

  return (
    <div className=" mx-auto">

      {/* Series Header */}
      <div className="relative text-center mb-12">

        <div>
          <img
              src={series.thumbnail}
              className="absolute inset-0 w-full h-full object-cover"
          />
        </div>

        {/* Overlay */}
        <div className="absolute inset-0 bg-black/70" />

        <div className={"relative z-20 py-7"}>
          {/* Back Button */}
          <Button variant="ghost" onClick={() => navigate('/series')} className="text-white absolute top-2 left-4">
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Series
          </Button>

          <div className="w-24 h-24 bg-gradient-to-br from-primary to-accent rounded-full flex items-center justify-center mx-auto mb-6">
            <Book className="w-12 h-12 text-primary-foreground" />
          </div>

          <Badge variant="secondary" className="bg-gray-300 mb-4">
            {seriesSermons.length} sermon{seriesSermons.length !== 1 ? 's' : ''}
          </Badge>

          <h1 className="text-4xl md:text-5xl font- text-white dark:text-foreground mb-4">
            {series.title}
          </h1>

          <p className="text-xl text-white dark:text-muted-foreground max-w-2xl mx-auto mb-6">
            {series.description}
          </p>

          {seriesSermons.length > 0 && (
              <div className="flex items-center justify-center gap-4 text-sm text-gray-300 dark:text-muted-foreground">
            <span className="flex items-center">
              <Calendar className="w-4 h-4 mr-1" />
              {new Date(seriesSermons[0].date).toLocaleDateString()} - {new Date(seriesSermons[seriesSermons.length - 1].date).toLocaleDateString()}
            </span>
              </div>
          )}
        </div>


      </div>

      {/* Sermons List */}
      {seriesSermons.length > 0 ? (
        <div className=" py-8 px-2 md:px-14 lg:px-17">
          <h2 className="text-xl bg-gray-300/40 dark:bg-gray-700 px-4 py-2 font-medium text-foreground rounded-t-full text-center">Sermons in this Series</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 px-2 mt-5">
            {seriesSermons.map((sermon, index) => (
              <Card key={sermon.id} className="group overflow-hidden hover:shadow-lg transition-all duration-300 border-border hover:border-primary/20">
                <CardHeader 
                  className="cursor-pointer p-0"
                  onClick={()=> navigate(`/sermons/${sermon.id}`)}
                >
                  <div className="aspect-video bg-gray-700 rounded-t-lg flex items-center justify-center group-hover:bg-primary/5 transition-colors relative overflow-hidden">
                    <div className="absolute top-3 left-3">
                      <Badge variant="secondary" className="bg-gray-800 text-gray-300 text-xs">
                        Part {index + 1}
                      </Badge>
                    </div>
                    <div className={"absolute z-20 bg-red-600 group-hover:bg-red-700 px-9 py-3 rounded-[10px] top-50 right-50"}>
                      <Play className="w-7 h-7 text-white transition-colors" />
                    </div>
                    <div className="absolute z-10 inset-0 bg-gradient-to-t from-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
                    <img
                      src={`https://i.ytimg.com/vi/${getYouTubeVideoId(sermon.videoUrl)}/hqdefault.jpg`}
                      className={"z-0 opacity-70"}
                    />
                  </div>
                </CardHeader>
                <CardContent className="p-6">
                  <CardTitle className="text-lg mb-2 dark:group-hover:text-primary transition-colors">
                    <Link to={`/sermons/${sermon.id}`} className="hover:underline">
                      {sermon.title}
                    </Link>
                  </CardTitle>
                  <CardDescription className="mb-4 line-clamp-2">
                    {sermon.description}
                  </CardDescription>
                  <div className="flex items-center justify-between text-sm text-gray-300 dark:text-muted-foreground">
                    <span>{sermon.preacher}</span>
                    <span className="flex items-center">
                      <Calendar className="w-4 h-4 mr-1" />
                      {new Date(sermon.date).toLocaleDateString()}
                    </span>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      ) : (
        <div className="text-center py-12">
          <div className="w-16 h-16 bg-muted rounded-full flex items-center justify-center mx-auto mb-4">
            <Play className="w-8 h-8 text-muted-foreground" />
          </div>
          <h3 className="text-xl font-semibold text-foreground mb-2">No sermons yet</h3>
          <p className="text-muted-foreground">
            Sermons for this series will appear here as they are added.
          </p>
        </div>
      )}
    </div>
  );
};

export default SeriesDetail;