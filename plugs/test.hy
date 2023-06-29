(defn reload [info]
  ((.get info "reload_plugs"))
  (return info))
(defn preload [info] 
  (.update info {"ctx" (+ (.get info "ctx") [["Reload Plugs" reload]])})
  (return info))
(defn reloaded [info] 
  (setv info (preload info))
  (return info))