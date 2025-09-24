import { useState, useEffect } from "react";
import { Sun, Moon } from "lucide-react";

const ThemeToggle = () => {
  const [isDarkMode, setIsDarkMode] = useState(
    window.matchMedia("(prefers-color-scheme: dark)").matches
  );

  useEffect(() => {
    document.documentElement.classList.toggle("dark", isDarkMode);
  }, [isDarkMode]);

  return (
    <button
      onClick={() => setIsDarkMode((prev) => !prev)}
      className="p-2 rounded bg-primary dark:bg-gray-800 text-primary-foreground flex items-center gap-2 transition-all duration-300 hover:scale-105"
    >
      {!isDarkMode ? (
        <>
          <Sun className="w-5 h-5 animate-spin-slow" />
          {/* <span>Light Mode</span> */}
        </>
      ) : (
        <>
          <Moon className="w-5 h-5 animate-pulse" />
          {/* <span>Dark Mode</span> */}
        </>
      )}
    </button>
  );
};

export default ThemeToggle;