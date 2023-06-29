; Plug. The parader plugin ecosystem
(setv plugs [])
(defn add_plug [p d]
  "Takes in the plugin name and the plugin module path."
  (.append plugs [p d]))