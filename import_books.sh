echo "import paged content"

# do taxonomy first
drush -y --userid=1 --uri=localhost:8000 migrate:import cmu_taxonomy_corporate_bodies
drush -y --userid=1 --uri=localhost:8000 migrate:import cmu_taxonomy_geo_locations
drush -y --userid=1 --uri=localhost:8000 migrate:import cmu_taxonomy_subjects

drush -y --userid=1 --uri=localhost:8000 migrate:import thistle_collection

drush -y --userid=1 --uri=localhost:8000 migrate:import thistle_page_files
# i don't think we need a media or file for the book.
drush -y --userid=1 --uri=http://localhost:8000 migrate:import thistle_book_nodes

drush -y --userid=1 --uri=http://localhost:8000 migrate:import thistle_page_nodes
# to connect the files to the nodes we need to make media
drush -y --userid=1 --uri=http://localhost:8000 migrate:import thistle_page_media