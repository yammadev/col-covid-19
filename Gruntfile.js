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
          style: 'expanded'
        },
        files: {
          'docs/css/main.css': 'resources/sass/main.sass'   // dest : src
        }
      }
    },

    // Babel
    babel: {
      options: {
        sourceMap: true,
        presets: ['@babel/preset-env']
      },
      dist: {
        files: {
          'docs/js/main.js': 'resources/js/main.js'   // dest : src
        }
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
  grunt.loadNpmTasks('grunt-babel');
  grunt.loadNpmTasks('grunt-html-build');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks

  // $ grunt build
  grunt.registerTask('build', ['sass', 'babel', 'htmlbuild', 'copy']);

  // $ grunt | $ grunt default
  grunt.registerTask('default', ['watch']);
};
