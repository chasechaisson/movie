import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Font -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" rel="stylesheet">

    <!-- Bootstrap 3 -->
    <script src="jquery-3.2.1.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <style type="text/css" media="screen">

        body {
            padding-top: 80px;
            font-family: "Roboto", sans-serif;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
            position: absolute;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
            z-index: 9003;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9004;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        h1 {
			font-family: 'Roboto', sans-serif;
			font-weight: 300;
			color: black;
			font-size: 30px
			padding: 40px;
		}
		h2 {
			font-family: 'Roboto', sans-serif;
			font-weight: 100;
			font-size: 20px;
			padding: 30px;
		}
		body {
			font-family: 'Roboto', sans-serif;
			padding-left: 20%;
			padding-right:20%;
			padding-top:5%;
			text-align: center;
		}
		head {
			font-family: 'Roboto', sans-serif;
		}
		a {
			text-decoration: none;
		}
        .butt {
            border-radius: 50%;
            width: 300px;
            height: 300px;
            color: black;
        }
        button {
            background-color: black
            border-color: none;
        }
        button:hover {
            background-color: gray;
            border-color: none;
        }
        .modal-content {
            overflow-y: auto;
            flex-direction: row;
            flex-wrap: wrap;
        }
        #trailer {
            z-index: 9002;
            position: fixed;
        }

        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
         jQuery(document).on('click', '.hanging-close', '.modal-backdrop', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            jQuery("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        jQuery(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = jQuery(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            jQuery("#trailer-video-container").empty().append(jQuery("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        jQuery(document).ready(function () {
          jQuery('.movie-tile').hide().first().show("fast", function showNext() {
            jQuery(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <div class="modal" id="movies">
      <div class="modal-dialog">
        <div class="modal-content">
        {movie_tiles}
        </div>
      </div>
    </div>

    <div class="modal" id="tvshows">
      <div class="modal-dialog">
        <div class="modal-content">
        {show_tiles}
        </div>
      </div>
    </div>

    <div class="container">
        <header class="row">
    		<h1 class="col-md-12, text-left">
    			MOVIES.DB
    		</h1>
    		</header>
    		<main>
    		      <div class="row">
    				<h2 class="col-md-6">
                        <button class="butt" data-toggle="modal" data-target="#movies">MOVIES
    					</button>
    				</h2>
    				<h2 class="col-md-6">
                        <button class="butt" data-toggle="modal" data-target="#tvshows">TV SHOWS
    				    </button>
    				</h2>
    			  </div>
    		</main>
    	</div>

  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-backdrop="static" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''
# A single tv show entry html
tvshow_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-backdrop="static" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="220">
    <h2>{show_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_description=movie.storyline
            )
    return content

def create_tv_tiles_content(tvshows):
    content = ''
    for tvshow in tvshows:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', tvshow.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', tvshow.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += tvshow_tile_content.format(
            show_title=tvshow.title,
            poster_image_url=tvshow.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            )
    return content

def open_movies_page(movies, tvshows):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        show_tiles=create_tv_tiles_content(tvshows))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
