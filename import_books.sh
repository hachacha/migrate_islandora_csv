echo "import paged content"

# jk lets try to see what happens with OCR.

drush -y --userid=1 --uri=localhost:8000 migrate:import thistlepagefiles
# i don't think we need a media or file for the book.
drush -y --userid=1 --uri=http://localhost:8000 migrate:import thistlebooknodes

drush -y --userid=1 --uri=http://localhost:8000 migrate:import thistlepagenodes
# to connect the files to the nodes we need to make media
drush -y --userid=1 --uri=http://localhost:8000 migrate:import thisetlepagemedia