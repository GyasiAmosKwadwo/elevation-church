import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { useAppContext } from "@/context/AppContext";
import { Play, Calendar, Users, Book, Clock, MapPin } from "lucide-react";
import { videos } from "@/assets/assets";
import { Badge } from "@/components/ui/badge";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import {getYouTubeVideoId} from "@/utili/utili";

const Home = () => {
  const { state } = useAppContext();
  const latestSermons = state.sermons.slice(0, 3);

  const sliderSettings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 4000,
    fade: true,
    pauseOnHover: true
  };

  const slideshowContent = [
    {
      type: 'video',
      src: videos.video_01,
      title: 'Live Worship Experience',
      description: 'Join us for powerful worship and prayer'
    },
    {
      type: 'video',
      src: videos.video_02,
      title: 'Community Fellowship',
      description: 'Building lasting relationships in faith'
    },
    {
      type: 'video',
      src: videos.video_03,
      title: 'Youth Ministry',
      description: 'Empowering the next generation'
    },
    {
      type: 'video',
      src: videos.video_04,
      title: 'Prayer & Healing',
      description: 'Experience God\'s miraculous power'
    }
  ];

  return (
    <div className="bg-gray-200 dark:bg-gray-900 overflow-hidden">
      {/* Hero Section with Video Background */}
      <section className="relative h-screen overflow-hidden">
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
        <div className="absolute inset-0 bg-black/50" />
        
        {/* Content */}
        <div className="relative z-10 h-full flex items-center justify-center text-white">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto text-center space-y-8">
              <h1 className="text-5xl md:text-7xl font-bold leading-tight animate-fade-in">
                Welcome to<br />
                <span className="bg-gradient-to-r from-accent to-gray-300 bg-clip-text text-transparent">
                  {state.churchSettings.name}
                </span>
              </h1>
              <p className="text-xl md:text-2xl text-white/90 max-w-2xl mx-auto animate-fade-in">
                Experience God's presence through powerful sermons, vibrant community, and life-changing encounters with Jesus Christ.
              </p>
              
              <div className="flex flex-col sm:flex-row gap-4 justify-center items-center animate-fade-in">
                {state.isLivestreaming && (
                  <Button size="lg" variant="secondary" asChild className="rounded group">
                    <a href={state.livestreamUrl} target="_blank" rel="noopener noreferrer">
                      <Play className="w-5 h-5 mr-2 group-hover:scale-110 transition-transform" />
                      Watch Live Now
                    </a>
                  </Button>
                )}
                <Button size="lg" variant="outline" asChild className="rounded border-white text-white hover:bg-white">
                  <Link to="/sermons">
                    <Book className="w-5 h-5 mr-2" />
                    Browse Sermons
                  </Link>
                </Button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="bg-blue-900/15">
        <div className="container mx-auto px-4 md:px-12 lg:px-20 py-16">
          <div className="grid grid-cols-1  md:grid-cols-2 lg:grid-cols-3 gap-8">
            <Card className="text-center p-4 space-y-4">
              <div className="w-16 h-16 bg-secondary dark:bg-gray-900 rounded-full flex items-center justify-center mx-auto">
                <Play className="w-8 h-8 text-primary-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-secondary dark:text-foreground">Live Streaming</h3>
              <p className="text-yellow-50 dark:text-muted-foreground">
                Join our live services from anywhere in the world and be part of our global community.
              </p>
            </Card>
            
            <Card className="text-center p-4 space-y-4">
              <div className="w-16 h-16 bg-secondary dark:bg-gray-900 rounded-full flex items-center justify-center mx-auto">
                <Book className="w-8 h-8 text-primary-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-secondary dark:text-foreground">Sermon Library</h3>
              <p className="text-yellow-50 dark:text-muted-foreground">
                Access hundreds of powerful messages organized by series and topics for easy discovery.
              </p>
            </Card>
            
            <Card className="text-center p-4 space-y-4 border-gray-500">
              <div className="w-16 h-16 bg-secondary dark:bg-gray-900 rounded-full flex items-center justify-center mx-auto">
                <Users className="w-8 h-8 text-primary-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-secondary dark:text-foreground">Community</h3>
              <p className="text-yellow-50 dark:text-muted-foregroundd">
                Connect with fellow believers and grow together in faith through our vibrant community.
              </p>
            </Card>
          </div>
        </div>
      </section>

      {/* Slideshow Section */}
      <section className="relative">
        <div className="w-full">
          <Slider {...sliderSettings}>
            {slideshowContent.map((slide, index) => (
              <div key={index} className="relative h-[70vh] overflow-hidden">
                {slide.type === 'video' ? (
                  <video 
                    autoPlay 
                    muted 
                    loop 
                    className="w-full h-full object-cover"
                  >
                    <source src={slide.src} type="video/mp4" />
                  </video>
                ) : (
                  <img 
                    src={slide.src} 
                    alt={slide.title}
                    className="w-full h-full object-cover"
                  />
                )}
                
                {/* Slide Overlay */}
                <div className="absolute inset-0 bg-black/40 flex items-center justify-center">
                  <div className="text-center text-white space-y-4 px-4">
                    <h3 className="text-4xl md:text-6xl font-bold">{slide.title}</h3>
                    <p className="text-xl md:text-2xl max-w-2xl mx-auto">{slide.description}</p>
                  </div>
                </div>
              </div>
            ))}
          </Slider>
        </div>
      </section>


      {/* Latest Sermons */}
      <section className="container mx-auto px-4 py-14 md:px-12 lg:px-20">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-blue-900 dark:text-foreground mb-2">
            Latest Sermons
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Discover life-transforming messages that will strengthen your faith and guide your spiritual journey.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {latestSermons.map((sermon) => (
            <Card key={sermon.id} className=" overflow-hidden group hover:shadow-lg transition-all duration-300 border-border hover:border-primary/20">
              <CardHeader className="p-0">
                <Link to={`/sermons/${sermon.id}`} className="aspect-video relative overflow-hidden bg-muted rounded-t-lg flex items-center justify-center group-hover:bg-primary/5 transition-colors">
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
                <CardTitle className="text-lg text-primary-foreground mb-2 hover:underline group-hover:text-gray-50 transition-colors">
                  <Link to={`/sermons/${sermon.id}`}>
                    {sermon.title}
                  </Link>
                </CardTitle>
                <CardDescription className=" mb-4 line-clamp-2">
                  {sermon.description}
                </CardDescription>
                <div className="flex items-center justify-between text-sm text-slate-400">
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

        <div className="text-center">
          <Button variant="secondary" size="lg" className="dark:bg-slate-700 rounded hover:shadow-xl" asChild>
            <Link to="/sermons">View All Sermons</Link>
          </Button>
        </div>
      </section>

      {/* Recent Events Slider */}
      <section className="container bg-blue-900/15 dark:bg-slate-800 mx-auto py-14 px-4">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-blue-900 dark:text-foreground mb-2">Upcoming Events</h2>
          <p className="text-lg text-gray-200 text-muted-foreground max-w-2xl mx-auto">Join us for these special gatherings</p>
        </div>
        
        <Slider {...{
          dots: false,
          infinite: true,
          speed: 500,
          slidesToShow: 2,
          slidesToScroll: 1,
          autoplay: true,
          autoplaySpeed: 3000,
          responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
              }
            },
            {
              breakpoint: 800,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
          ]
        }} className="events-slider mb-16">
          {state.events.filter(event => event.featured).map((event) => (
            <div key={event.id} className="px-2">
              <Card className="h-full hover:shadow-lg transition-shadow">
                <div className="relative">
                  <img 
                    src={event.image} 
                    alt={event.title}
                    className="w-full h-48 object-cover rounded-t-lg"
                  />
                  <div className="absolute top-4 left-4">
                    <Badge className="bg-slate-950 text-primary-foreground">
                      {new Date(event.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                    </Badge>
                  </div>
                </div>
                <CardHeader>
                  <CardTitle className="text-slate-100 text-2xl">{event.title}</CardTitle>
                </CardHeader>
                <CardContent className="space-y-2">
                  <p className="text-sm text-gray-300 line-clamp-2">{event.description}</p>
                  <div className="flex items-center text-xs text-slate-400">
                    <Clock className="w-3 h-3 mr-1" />
                    {new Date(`2000-01-01T${event.time}`).toLocaleTimeString('en-US', {
                      hour: 'numeric',
                      minute: '2-digit',
                      hour12: true
                    })}
                  </div>
                  <div className="flex items-center text-xs text-slate-400">
                    <MapPin className="w-3 h-3 mr-1" />
                    {event.location}
                  </div>
                  <div className="pt-2">
                    <Link to={`/events/${event.id}`}>
                      <Button variant="secondary" size="sm" className="bg-slate-200 rounded w-full">Learn More</Button>
                    </Link>
                  </div>
                </CardContent>
              </Card>
            </div>
          ))}
        </Slider>
      </section>


      {/* Features */}
      <section className="">
        <div className="container mx-auto px-4 md:px-12 lg:px-20 py-16">
          <div className="grid grid-cols-1  md:grid-cols-2 lg:grid-cols-3 gap-8">
            <Card className="text-center p-4 space-y-4">
              <div className="w-16 h-16 bg-secondary dark:bg-gray-900 rounded-full flex items-center justify-center mx-auto">
                <Play className="w-8 h-8 text-primary-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-secondary dark:text-foreground">Live Streaming</h3>
              <p className="text-yellow-50 dark:text-muted-foreground">
                Join our live services from anywhere in the world and be part of our global community.
              </p>
            </Card>
            
            <Card className="text-center p-4 space-y-4">
              <div className="w-16 h-16 bg-secondary dark:bg-gray-900 rounded-full flex items-center justify-center mx-auto">
                <Book className="w-8 h-8 text-primary-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-secondary dark:text-foreground">Sermon Library</h3>
              <p className="text-yellow-50 dark:text-muted-foreground">
                Access hundreds of powerful messages organized by series and topics for easy discovery.
              </p>
            </Card>
            
            <Card className="text-center p-4 space-y-4 border-gray-500">
              <div className="w-16 h-16 bg-secondary dark:bg-gray-900 rounded-full flex items-center justify-center mx-auto">
                <Users className="w-8 h-8 text-primary-foreground" />
              </div>
              <h3 className="text-xl font-semibold text-secondary dark:text-foreground">Community</h3>
              <p className="text-yellow-50 dark:text-muted-foregroundd">
                Connect with fellow believers and grow together in faith through our vibrant community.
              </p>
            </Card>
          </div>
        </div>
      </section>

    </div>
  );
};

export default Home;