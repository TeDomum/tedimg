var gulp = require('gulp'), 
    bower = require('gulp-bower'),
    replace = require('gulp-replace'),
    concat = require('gulp-concat');

var config = {
     srcPath: './resources',
     bowerDir: './bower_components' ,
    dstPath: './tedimg/static'
}

gulp.task('bower', function() { 
    return bower()
     .pipe(gulp.dest(config.bowerDir)) 
});

gulp.task('styles', function () {
    return gulp.src([
        config.bowerDir + '/*/dist/css/*.min.css',
        config.srcPath + '/main.css'
      ])
      .pipe(concat('main.css'))
      .pipe(replace("/font/", "/static/font/"))
      .pipe(gulp.dest(config.dstPath))
});

gulp.task('scripts', function() {
    return gulp.src([
        config.bowerDir + '/jquery/dist/jquery.min.js',
        config.bowerDir + '/Materialize/dist/js/materialize.min.js',
        config.srcPath + '/*.js'
      ])
      .pipe(concat('main.js'))
      .pipe(gulp.dest(config.dstPath))
});

gulp.task('copy', function() {
    return gulp.src(config.bowerDir + '/Materialize/dist/font/**/*')
    .pipe(gulp.dest(config.dstPath + '/font'));
});

  gulp.task('default', ['bower', 'styles', 'copy', 'scripts']);
