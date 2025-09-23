import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="bg-gray-300  dark:bg-gray-950 border-t border-border">
      <div className="container mx-auto px-4 pt-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 px-4 md:px-12 lg:px-20">
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-6 h-6 bg-primary rounded-full flex items-center justify-center">
                <span className="text-primary-foreground font-bold text-xs">E</span>
              </div>
              <span className="font-bold text-foreground">Elevation Church</span>
            </div>
            <p className="text-sm text-muted-foreground">
              Elevating lives through the power of God's word and community fellowship.
            </p>
          </div>
          
          <div>
            <h3 className="font-semibold text-foreground mb-4">Quick Links</h3>
            <div className="space-y-2">
              <Link to="/sermons" className="block text-sm text-muted-foreground hover:text-primary transition-colors">
                Sermons
              </Link>
              <Link to="/series" className="block text-sm text-muted-foreground hover:text-primary transition-colors">
                Series
              </Link>
            </div>
          </div>
          
          <div>
            <h3 className="font-semibold text-foreground mb-4">Connect</h3>
            <div className="space-y-2">
              <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" className="block text-sm text-muted-foreground hover:text-primary transition-colors">
                YouTube
              </a>
              <a href="https://podcast.com" target="_blank" rel="noopener noreferrer" className="block text-sm text-muted-foreground hover:text-primary transition-colors">
                Podcast
              </a>
            </div>
          </div>
          
          <div>
            <h3 className="font-semibold text-foreground mb-4">Contact</h3>
            <p className="text-sm text-muted-foreground">
              123 Church Street<br />
              City, State 12345<br />
              (555) 123-4567
            </p>
          </div>
        </div>
        
        <div className="border-t border-border my-3 pt-4 text-center">
          <p className="text-xs text-muted-foreground">
            © 2024 Elevation Church. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;