// Wrapper
module.exports = function(grunt) {
  // Configuration
  grunt.initConfig({
    // Package
    pkg: grunt.file.readJSON('package.json'),

    // Sass
    sass: {
      dist: {
        options: {
          // sourceMap: true,
          // style: 'expanded'    // expanded (Dev purposes)
          style: 'compressed'
        },
        files: {        // output : input
          'docs/css/main.min.css': 'resources/sass/main.sass'
        }
      }
    },

    // uglify
    uglify: {
      options: {
        // beautify: true,        // expanded (Dev purposes)
        sourceMap: true
      },
      build: {
        src: [                          // input
          'resources/data/*.js',
          'resources/js/*.js'
        ],
        dest: 'docs/js/main.min.js'     // output
      }
    },

    // Html build
    htmlbuild: {
      dist: {
        src: 'resources/index.html',    // source
        dest: 'docs/',                  // destination
        options: {
          beautify: true,   // expanded
          styles: {         // scripts passed to template
            main: 'docs/css/main.min.css'
          },
          scripts: {        // scripts passed to template
            main: 'docs/js/main.min.js'
          },
          data: {           // data passed to template
            updated: '<%= grunt.template.today("dd-mm-yyyy HH:MM:ss TT Z") %>'
          }
        }
      }
    },

    // Copy
    copy: {
      main: {
        files: [
          {
            expand: true,
            cwd: 'resources/imgs',    // source
            src: '*.svg',             // extension
            dest: 'docs/imgs'         // destination
          },
          {
            expand: true,
            cwd: 'resources/fonts',   // source
            src: '**',                // extension
            dest: 'docs/fonts'        // destination
          }
        ]
      }
    },

    // Watch for changes (Dev purposes)
    watch: {
      sass: {
        files: [
          'resources/sass/*.sass',
          'resources/js/*.js',
          'resources/*.html'
        ],
        tasks: ['build']
      }
    }
  });

  // Load
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-html-build');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register

  // grunt build
  grunt.registerTask('build', ['sass', 'uglify', 'copy', 'htmlbuild']);

  // grunt | $ grunt default
  grunt.registerTask('default', ['build']);
};
