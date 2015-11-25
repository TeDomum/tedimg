var gulp = require('gulp'), 
    sass = require('gulp-ruby-sass') 
    notify = require("gulp-notify") 
    bower = require('gulp-bower');

var config = {
     srcPath: './resources',
     bowerDir: './bower_components' ,
    dstPath: './tedimg/static'
}

var cssPath = [
    config.srcPath,
    config.bowerDir + '/Materialize/sass',
]

gulp.task('bower', function() { 
    return bower()
     .pipe(gulp.dest(config.bowerDir)) 
});

gulp.task('styles', function () {
    return sass(config.srcPath + '/main.scss', {loadPath: cssPath})
    .on('error', sass.logError)
    .pipe(gulp.dest(config.dstPath))
});

  gulp.task('default', ['bower', 'styles']);
