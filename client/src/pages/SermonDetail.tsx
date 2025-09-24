import { useParams, Link, useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { useAppContext } from "@/context/AppContext";
import { Play, Download, Calendar, Tag, ArrowLeft,SendIcon, ExternalLink, ChevronLeft, ChevronRight } from "lucide-react";
import { toast } from "@/hooks/use-toast";
import {useEffect} from "react";
import {getYouTubeVideoId} from "@/utili/utili";

const SermonDetail = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { state } = useAppContext();
  
  const sermon = state.sermons.find(s => s.id === id);
  const youtubeID = getYouTubeVideoId(sermon.videoUrl)

  // useEffect(()=>{
  //   const youtubeID = getYouTubeVideoId(sermon.videoUrl)
  // },[])
  
  if (!sermon) {
    return (
      <div className="container h-full mx-auto px-4 md:px-16 lg:px-20 py-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-foreground mb-4">Sermon Not Found</h1>
          <p className="text-muted-foreground mb-6">The sermon you're looking for doesn't exist.</p>
          <Button variant={"secondary"} onClick={() => navigate('/sermons')}>
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Sermons
          </Button>
        </div>
      </div>
    );
  }

  const seriesSermons = sermon.series ? 
    state.sermons.filter(s => s.series === sermon.series) : [];
  const currentIndex = seriesSermons.findIndex(s => s.id === sermon.id);
  const prevSermon = currentIndex > 0 ? seriesSermons[currentIndex - 1] : null;
  const nextSermon = currentIndex < seriesSermons.length - 1 ? seriesSermons[currentIndex + 1] : null;

  const handleShare = () => {
    if (navigator.share) {
      navigator.share({
        title: sermon.title,
        text: sermon.description,
        url: window.location.href,
      });
    } else {
      navigator.clipboard.writeText(window.location.href);
      toast({
        title: "Link copied!",
        description: "Sermon link has been copied to your clipboard.",
      });
    }
  };

  return (
    <div className="container bg-grayc-950/80 mx-auto px-4 md:px-14 lg:px-17 pb-8">
      {/* Back Button */}
      <Button variant="ghost" onClick={() => navigate('/sermons')} className="mb-4">
        <ArrowLeft className="w-4 h-4 mr-2" />
        Back to Sermons
      </Button>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Main Content */}
        <div className="lg:col-span-2 space-y-6">
          {/* Video Player */}
          <Card className={"overflow-hidden "}>
            <CardContent className="p-0 ">
              <div className="aspect-video bg-gray-900 rounded-t-lg flex items-center justify-center">

                <iframe
                    // width="560" height="315"
                    className={"size-full"}
                    src={`https://www.youtube.com/embed/${youtubeID}`}
                    title="YouTube video player"
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerPolicy="strict-origin-when-cross-origin"
                    allowFullScreen>
                </iframe>

              </div>
            </CardContent>
          </Card>

          {/* Sermon Info */}
          <div className="space-y-6">
            <div>
              {sermon.series && (
                <Link 
                  to={`/series/${state.series.find(s => s.title === sermon.series)?.id}`}
                  className="inline-block px-3 py-1 text-sm font-medium bg-primary/10 text-primary rounded-full mb-3 hover:bg-primary/20 transition-colors"
                >
                  {sermon.series}
                </Link>
              )}
              <h1 className="text-3xl md:text-4xl font-bold text-blue-900 dark:text-foreground mb-4">
                {sermon.title}
              </h1>
              <div className="flex flex-wrap items-center gap-4 text-gray-800 dark:text-muted-foreground mb-6">
                <span className="font-medium">{sermon.preacher}</span>
                <span className="flex items-center">
                  <Calendar className="w-4 h-4 mr-1" />
                  {new Date(sermon.date).toLocaleDateString('en-US', { 
                    year: 'numeric', 
                    month: 'long', 
                    day: 'numeric' 
                  })}
                </span>
              </div>
            </div>

            <div className="prose prose-gray max-w-none">
              <p className="text-lg text-gray-800 dark:text-muted-foreground leading-relaxed">
                {sermon.description}
              </p>
            </div>

            {sermon.tags.length > 0 && (
              <div>
                <h3 className="text-lg font-semibold text-foreground mb-3 flex items-center">
                  <Tag className="w-5 h-5 mr-2" />
                  Topics
                </h3>
                <div className="flex flex-wrap gap-2">
                  {sermon.tags.map((tag) => (
                    <span
                      key={tag}
                      className="inline-block px-3 py-1 text-sm bg-gray-300 dark:bg-gray-800 text-gray-800 dark:text-muted-foreground rounded-full"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            )}

            <div className="flex gap-4">
              <Button onClick={handleShare} className={"rounded- border-gray-700 px-5 gap-3" } variant="outline">
                Share Sermon
                <SendIcon />
              </Button>
            </div>
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Series Navigation */}
          {sermon.series && seriesSermons.length > 1 && (
            <Card>
              <CardHeader>
                <CardTitle className="text-lg">{sermon.series}</CardTitle>
                {/*<CardDescription>{sermon.series}</CardDescription>*/}
              </CardHeader>
              <CardContent className="space-y-2">
                {prevSermon && (
                  <Link to={`/sermons/${prevSermon.id}`}>
                    <div className="flex items-center p-3 rounded border border-border hover:bg-slate-900 transition-colors">
                      <ChevronLeft className="w-4 h-4 mr-2 text-muted-foreground" />
                      <div className="flex-1 min-w-0">
                        <p className="text-xs text-muted-foreground">Previous</p>
                        <p className="text-sm text-gray-400 font-medium truncate">{prevSermon.title}</p>
                      </div>
                    </div>
                  </Link>
                )}
                
                {nextSermon && (
                  <Link to={`/sermons/${nextSermon.id}`}>
                    <div className="flex items-center mt-3 p-3 rounded border border-border hover:bg-slate-900  transition-colors">
                      <div className="flex-1 min-w-0">
                        <p className="text-xs text-muted-foreground">Next</p>
                        <p className="text-sm text-gray-400 font-medium truncate">{nextSermon.title}</p>
                      </div>
                      <ChevronRight className="w-4 h-4 ml-2 text-muted-foreground" />
                    </div>
                  </Link>
                )}
              </CardContent>
            </Card>
          )}

          {/* Related Sermons */}
          <Card className={"o overflow-x-hidden"}>
            <CardHeader className={"p-0"}>
              <CardTitle className="bg-blue-500/20 dark:bg-gray-700 py-2 text-center text-lg">More Sermons</CardTitle>
            </CardHeader>
            <CardContent className="overflow-y-auto space-y-2 max-h-[350px] mt-3">
              {state.sermons
                .filter(s => s.id !== sermon.id)
                .slice(0, 3)
                .map((relatedSermon) => (
                  <Link key={relatedSermon.id} to={`/sermons/${relatedSermon.id}`}>
                    <div className="flex items-start space-x-3 p-3 rounded hover:bg-slate-900/40 dark:hover:bg-slate-900 transition-colors">
                      <div className="w-16 h-12 bg-muted rounded flex items-center justify-center flex-shrink-0">
                        {/* <Play className="absolute w-12 h-12 text-muted-foreground group-hover:text-primary transition-colors" /> */}
                        <img
                          className="w-full hover:opacity-40 object-cover"
                          src={`https://i.ytimg.com/vi/${getYouTubeVideoId(sermon.videoUrl)}/hqdefault.jpg`}
                        />
                      </div>
                      <div className="flex-1 min-w-0">
                        <p className="text-sm font-medium text-gray-300 dark:text-foreground truncate">
                          {relatedSermon.title}
                        </p>
                        <p className="text-xs  text-gray-300 dark:text-muted-foreground">
                          {relatedSermon.preacher}
                        </p>
                        <p className="text-xs text-muted-foreground">
                          {new Date(relatedSermon.date).toLocaleDateString()}
                        </p>
                      </div>
                    </div>
                  </Link>
                ))}
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default SermonDetail;