import { useState } from "react";
import { Link } from "react-router-dom";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useAppContext } from "@/context/AppContext";
import { Search, Play, Calendar, Filter } from "lucide-react";
import {videos} from "@/assets/assets";
import {getYouTubeVideoId} from "@/utili/utili";
import {Select, SelectContent, SelectItem, SelectTrigger, SelectValue} from "@/components/ui/select";

const Sermons = () => {
  const { state } = useAppContext();
  const [searchTerm, setSearchTerm] = useState("");
  const [showDropdown, setShowDropdown] = useState(false);
  const [selectedSeries, setSelectedSeries] = useState<string>("");

  const filteredSermons = state.sermons.filter((sermon) => {
    const matchesSearch = sermon.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         sermon.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         sermon.preacher.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         sermon.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase()));
    
    const matchesSeries = !selectedSeries || sermon.series === selectedSeries;
    
    return matchesSearch && matchesSeries;
  });

  const uniqueSeries = [...new Set(state.sermons.map(sermon => sermon.series).filter(Boolean))];

  return (
    <div className=" ">
      {/* Header */}
      <section className="relative h- overflow-hidden">
          {/* Background Video */}
          <video
              autoPlay
              muted
              loop
              className="absolute inset-0 w-full h-full object-cover"
          >
              <source src={videos.heroVideo} type="video/mp4" />
          </video>

          {/* Overlay */}
          <div className="absolute inset-0 bg-black/70" />

          <div className={"relative h-full flex flex-col items-center justify-center mt-10 px-5 z-10"}>
              <div className="text-center mb-12">
                  <h1 className="text-4xl md:text-5xl font-bold text-white dark:text-foreground mb-4">
                      Sermons
                  </h1>
                  <p className="text-xl text-white darktext-muted-foreground max-w-2xl mx-auto">
                      Explore our complete collection of powerful messages designed to inspire, encourage, and strengthen your faith journey.
                  </p>
              </div>

              {/* Search and Filter */}
              <div className="mb-8 space-y-4">
                  <div className="relative max-w-lg mx-auto">
                      <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground w-4 h-4" />
                      <Input
                          placeholder="Search sermons, topics, or preachers..."
                          value={searchTerm}
                          onChange={(e) => setSearchTerm(e.target.value)}
                          className="pl-10"
                      />
                  </div>

                  {/*<div>*/}
                  {/*    <Select value={selectedSeries} onValueChange={(value) => selectedSeries(value)}>*/}
                  {/*        <SelectTrigger>*/}
                  {/*            <SelectValue placeholder="Select a series" />*/}
                  {/*        </SelectTrigger>*/}
                  {/*        <SelectContent>*/}
                  {/*            <SelectItem  value="gdg">No Series</SelectItem>*/}
                  {/*            {state.series.map((series) => (*/}
                  {/*                <SelectItem key={series.id} value={series.title}>*/}
                  {/*                    {series.title}*/}
                  {/*                </SelectItem>*/}
                  {/*            ))}*/}
                  {/*        </SelectContent>*/}
                  {/*    </Select>*/}
                  {/*</div>*/}
                  
                  <div className="flex flex-wrap justify-center gap-2">
                      <Button
                          variant={selectedSeries === "" ? "secondary" : "outline"}
                          size="sm"
                          className={"rounded-full px-4"}
                          onClick={() => setSelectedSeries("")}
                      >
                          All Series
                      </Button>
                      {uniqueSeries.map((series) => (
                          <Button
                              key={series}
                              variant={selectedSeries === series ? "secondary" : "outline"}
                              size="sm"
                              className={"text-white rounded-full px-4"}
                              onClick={() => setSelectedSeries(series || "")}
                          >
                              {series}
                          </Button>
                      ))}
                  </div>

                  {/* Results count */}
                  <div className="mb-6 mx-auto">
                      <p className="mx-auto text-center w-fit px-4 py-1 rounded text-sm text-slate-600 bg-slate-100">
                          {filteredSermons.length} sermon{filteredSermons.length !== 1 ? 's' : ''} found
                      </p>
                  </div>
              </div>
          </div>

      </section>




      {/* Sermons Grid */}
      <div className=" grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 py-8 px-4 md:px-14 lg:px-17 gap-6">
        {filteredSermons.map((sermon) => (
          <Card key={sermon.id} className="group overflow-hidden hover:shadow-lg transition-all duration-300 border-border hover:border-primary/20">
            <CardHeader className="cursor-pointer p-0">
              <Link to={`/sermons/${sermon.id}`}>
              <div className="aspect-video bg-gray-700 rounded-t-lg flex items-center justify-center group-hover:bg-primary/5 transition-colors relative overflow-hidden">
                <div className={"absolute z-20 bg-red-600 group-hover:bg-red-700 px-9 py-3 rounded-[10px] top-50 right-50"}>
                    <Play className="w-7 h-7 text-white transition-colors" />
                </div>
                <div className="absolute z-10 inset-0 bg-gradient-to-t from-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
                <img
                    src={`https://i.ytimg.com/vi/${getYouTubeVideoId(sermon.videoUrl)}/hqdefault.jpg`}
                    className={"z-0 opacity-70"}
                />
              </div>
              </Link>

            </CardHeader>
            <CardContent className="p-6">
              <div className="mb-2">
                {sermon.series && (
                  <span className="inline-block px-2 py-1 text-xs font-medium bg-blue-700/30 dark:bg-primary/10 text-gray-300 dark:text-primary rounded-full mb-2">
                    {sermon.series}
                  </span>
                )}
              </div>
              <CardTitle className="text-lg mb-2 dark:group-hover:text-primary transition-colors">
                <Link to={`/sermons/${sermon.id}`} className="hover:underline">
                  {sermon.title}
                </Link>
              </CardTitle>
              <CardDescription className="mb-4 line-clamp-2">
                {sermon.description}
              </CardDescription>
              <div className="space-y-4">
                <div className="flex items-center justify-between text-sm text-muted-foreground">
                  <span className="font-medium">{sermon.preacher}</span>
                  <span className="flex items-center">
                    <Calendar className="w-4 h-4 mr-1" />
                    {new Date(sermon.date).toLocaleDateString()}
                  </span>
                </div>
                {sermon.tags.length > 0 && (
                  <div className="flex flex-wrap gap-1">
                    {sermon.tags.slice(0, 3).map((tag) => (
                      <span
                        key={tag}
                        className="inline-block px-3 py-2 text-xs bg-gray-200 dark:bg-gray-900 text-muted-foreground rounded"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {filteredSermons.length === 0 && (
        <div className="text-center py-12">
          <div className="w-16 h-16 bg-muted rounded-full flex items-center justify-center mx-auto mb-4">
            <Search className="w-8 h-8 text-muted-foreground" />
          </div>
          <h3 className="text-xl font-semibold text-foreground mb-2">No sermons found</h3>
          <p className="text-muted-foreground mb-4">
            Try adjusting your search terms or clearing the filters.
          </p>
          <Button variant="outline" onClick={() => {
            setSearchTerm("");
            setSelectedSeries("");
          }}>
            Clear Filters
          </Button>
        </div>
      )}
    </div>
  );
};

export default Sermons;