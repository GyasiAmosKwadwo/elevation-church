import { Link, useNavigate } from "react-router-dom";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { useAppContext } from "@/context/AppContext";
import {Book, Play, Search} from "lucide-react";
import {videos} from "@/assets/assets";
import { useState } from "react";
import {Input} from "@/components/ui/input";

const Series = () => {
  const { state } = useAppContext();
  const [searchTerm, setSearchTerm] = useState("");
  const navigate = useNavigate();


  const filteredSeries = state.series.filter((series) => {
    const matchesSearch = series.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         series.description.toLowerCase().includes(searchTerm.toLowerCase())
    
    
    return matchesSearch;
  });

  return (
    <div className="">
      {/* Header */}
      <section className="relative h-[390px] overflow-hidden">
          {/* Background Video */}
          <video
              autoPlay
              muted
              loop
              className="absolute inset-0 w-full h-full object-cover"
          >
              <source src={videos.video_03} type="video/mp4" />
          </video>

          {/* Overlay */}
          <div className="absolute inset-0 bg-black/70" />

          <div className="relative h-full flex flex-col items-center justify-center z-20 px-5 text-center mb-12">
              <h1 className="text-4xl md:text-5xl font-bold text-white dark:text-foreground mb-4">
                  Sermon Series
              </h1>
              <p className="text-xl text-white dark:text-muted-foreground max-w-2xl mx-auto">
                  Discover organized collections of sermons that dive deep into specific themes, books of the Bible, and spiritual topics.
              </p>

              <div className={"w-full"}>
                  <div className="relative max-w-lg md mx-auto mt-9">
                      <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground w-4 h-4" />
                      <Input
                          placeholder="Search sermons, topics, or preachers..."
                          value={searchTerm}
                          onChange={(e) => setSearchTerm(e.target.value)}
                          className="pl-10 "
                      />
                  </div>
              </div>

          </div>
      </section>

      {/* Series Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 py-8 px-4 md:px-14 lg:px-17">
        {filteredSeries.map((series) => {
          const sermonCount = series.sermons.length;
          const latestSermon = state.sermons
            .filter(sermon => series.sermons.includes(sermon.id))
            .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())[0];

          return (
            <Card  key={series.id} className="group hover:shadow-lg overflow-hidden transition-all duration-300 border-border hover:border-primary/20">
              <CardHeader onClick={()=> navigate(`/series/${series.id}`)} className="relative p-0">
                <div className=" aspect-video bg-gradient-to-br from-primary/10 to-accent/10 rounded-t-lg flex items-center justify-center group-hover:from-primary/20 group-hover:to-accent/20 transition-all">
                  <Book className="absolute top-50 right-50 w-12 z-20 h-12 text-primary group-hover:scale-110 transition-transform" />
                  <img src={series.thumbnail} className={"w-full object-contain opacity-95 hover:opacity-50"} />
                </div>
              </CardHeader>
              <CardContent className="p-6">
                <div className="flex items-start justify-between mb-3">
                  <Badge variant="secondary" className="bg-gray-300 text-xs">
                    {sermonCount} sermon{sermonCount !== 1 ? 's' : ''}
                  </Badge>
                  {latestSermon && (
                    <span className="text-xs text-gray-300 dark:text-muted-foreground">
                      Latest: {new Date(latestSermon.date).toLocaleDateString()}
                    </span>
                  )}
                </div>
                
                <CardTitle className="text-xl mb-3  dark:group-hover:text-primary transition-colors">
                  <Link to={`/series/${series.id}`} className="hover:underline">
                    {series.title}
                  </Link>
                </CardTitle>
                
                <CardDescription className="mb-4 line-clamp-3">
                  {series.description}
                </CardDescription>

                {latestSermon && (
                  <div className="border-t border-border pt-4">
                    <p className="text-sm text-gray-300 dark:text-muted-foreground mb-1">Latest Sermon:</p>
                    <Link 
                      to={`/sermons/${latestSermon.id}`}
                      className="text-sm font-medium hover:underline text-gray-200 dark:text-foreground hover:text-gray-500 transition-colors flex items-center"
                    >
                      <Play className="w-3 h-3 mr-2" />
                      {latestSermon.title}
                    </Link>
                  </div>
                )}
              </CardContent>
            </Card>
          );
        })}
      </div>

      {state.series.length === 0 && (
        <div className="text-center py-12">
          <div className="w-16 h-16 bg-muted rounded-full flex items-center justify-center mx-auto mb-4">
            <Book className="w-8 h-8 text-muted-foreground" />
          </div>
          <h3 className="text-xl font-semibold text-foreground mb-2">No series available</h3>
          <p className="text-muted-foreground">
            Sermon series will appear here as they are created.
          </p>
        </div>
      )}
    </div>
  );
};

export default Series;