(import src.main :as main)
(import src.plug :as plug)
(plug.add_plug "base" "plugs.base")
; !!! YOUR PLUGIN DEFINITIONS GO HERE !!!
(plug.add_plug "test" "plugs.test")
;; Call main function
(main.main)