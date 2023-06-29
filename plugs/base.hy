;; Needed for the browser to work properly.
(defn preload [info]
  "Adds the default bookmarks and displays the ``Preloading...`` message."
  (print "Preloading...")
  (.update info {"bookmarks" (+ (.get info "bookmarks") [["google" "https://google.com"] ["poggingfish" "https://pogging.fish"]])})
  (return info))
(defn onload [info]
  "Displays the amount of time it took to load"
  (print (+ "Loaded in " (str (.get info "load_time")) " seconds!")) 
  (return info))
(defn bookmark_clicked [info bookmark]
  "Changes the URL when you click a bookmark"
  (.update info {"current_url" bookmark})
  ((.get info "change_url_call"))
  (return info))
(defn return_url_bar [info url]
  "Changes the current site to the site on the URL bar when you press enter."
  (.update info {"current_url" url}) 
  ((.get info "change_url_call"))
  (return info))
(defn url_changed [info url]
  "Changes the URL bar when the url of the webview changes."
  (.update info {"current_url" url})
  ((.get info "update_url_bar_call"))
  (return info))
(defn refresh [info]
  "Handles refreshing when you press F5/The refresh button"
  (print "Refreshing!")
  ((.get info "refresh_call"))
  (return info))
(defn add_bookmark [info url] 
  "Adds a new bookmark!"
  (.update info {"bookmarks" (+ (.get info "bookmarks") [[url url]])})
  ((.get info "reload_bookmarks")))