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
          style: 'expanded'
        },
        files: {
          'docs/css/main.css': 'resources/sass/main.sass'   // dest : src
        }
      }
    },

    // uglify
    uglify: {
      options: {
        beautify: true,
        sourceMap: true,
      },
      build: {
        src: 'resources/js/main.js',    // src
        dest: 'docs/js/main.js'         // dest
      }
    },

    // Html build
    htmlbuild: {
      dist: {
        src: 'resources/index.html',    // src
        dest: 'docs/',                  // dest
        options: {
          beautify: true,
          styles: {
            main: 'docs/css/main.css'
          },
          scripts: {
            main: 'docs/js/main.js'
          },
          data: {
            updated: '<%= grunt.template.today("dd-mm-yyyy HH:MM:ss TT Z") %>'
          }
        }
      }
    },

    // Copy
    copy: {
      main: {
        files: [{
          expand: true,
          cwd: 'resources/imgs',    // src
          src: '*.svg',
          dest: 'docs/imgs'         // dest
        }]
      }
    },

    // Watch for changes
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

  // Load plugins
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-html-build');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks

  // $ grunt build-assets
  grunt.registerTask('build-assets', ['sass', 'uglify', 'copy']);

    // $ grunt build-html
  grunt.registerTask('build-html', ['htmlbuild']);

  // $ grunt build
  grunt.registerTask('build', ['build-assets', 'build-html']);

  // $ grunt | $ grunt default
  grunt.registerTask('default', ['watch']);
};
