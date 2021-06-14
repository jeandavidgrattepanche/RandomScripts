install.packages(c("cowplot", "googleway", "ggplot2", "ggrepel", "ggspatial", "libwgeom", "sf", "rnaturalearth", "rnaturalearthdata","rgeos"))
library("ggplot2")
theme_set(theme_bw())
library("sf")
library("rnaturalearth")
library("rnaturalearthdata")
library("ggspatial")
world <- ne_countries(scale = "medium", returnclass = "sf")
class(world)
#world_points<- st_centroid(world)
#world_points <- cbind(world, st_coordinates(st_centroid(world$geometry)))

station <- read.table('~/Documents/GitHub/RandomScripts/Antarctica_map_station.txt', header = TRUE)

ggplot(data = world) +
	geom_sf() +
#	geom_text(data= world_points,aes(x=X, y=Y, label=name),color = "darkblue", fontface = "bold", check_overlap = FALSE) +
	geom_point(data= station, aes(x = longitude, y = latitude), size = 2, shape = 23, fill = station$gcolor ) +
	geom_text(data= station,aes(x= longitude - 0.3, y= latitude, label=station),color = station$gcolor,  check_overlap = FALSE) +	
	annotation_scale(location = "br", width_hint = 0.5) +
	annotation_north_arrow(location = "br", which_north = "true", pad_x = unit(0.75, "in"), pad_y = unit(0.5, "in"), style = north_arrow_fancy_orienteering) +
	coord_sf(xlim = c(-70.5, -58.2), ylim = c(-68.9, -63.5), expand = FALSE)
	
# version 2 of the map... more fine scale of the coastline
library(mapdata)

world2 <- map("worldHires", fill = T, plot = F)
world2 <- st_as_sf(world2)
ggplot(data = world2) +
	geom_sf() +
#	geom_text(data= world_points,aes(x=X, y=Y, label=name),color = "darkblue", fontface = "bold", check_overlap = FALSE) +
	geom_point(data= station, aes(x = longitude, y = latitude), size = 2, shape = 23, fill = station$gcolor ) +
	geom_text(data= station,aes(x= longitude - 0.3, y= latitude, label=station),color = station$gcolor,  check_overlap = FALSE) +	
	annotation_scale(location = "br", width_hint = 0.5) +
	annotation_north_arrow(location = "br", which_north = "true", pad_x = unit(0.75, "in"), pad_y = unit(0.5, "in"), style = north_arrow_fancy_orienteering) +
	coord_sf(xlim = c(-70.5, -58.2), ylim = c(-68.9, -63.5), expand = FALSE)