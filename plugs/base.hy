;; Needed for the browser to work properly.
(defn preload [info]
  (print "Preloading...")
  (.update info {"bookmarks" (+ (.get info "bookmarks") [["google" "https://google.com"] ["poggingfish" "https://pogging.fish"]])})
  (return info))
(defn onload [info]
  (print (+ "Loaded in " (str (.get info "load_time")) " seconds!")) 
  (return info))
(defn bookmark_clicked [info bookmark]
  (.update info {"current_url" bookmark})
  ((.get info "change_url_call"))
  (return info))
(defn return_url_bar [info url]
  (.update info {"current_url" url}) 
  ((.get info "change_url_call"))
  (return info))
(defn url_changed [info url]
  (print url)
  (.update info {"current_url" url})
  ((.get info "update_url_bar_call"))
  (return info))
(defn refresh [info]
  (print "Refreshing!")
  ((.get info "refresh_call"))
  (return info))