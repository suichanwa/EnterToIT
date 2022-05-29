const gulp = require('gulp');
const { src, dest } = require('gulp');
const babel = require('gulp-babel');
const uglify = require('gulp-uglify');
const rename = require('gulp-rename');
const fileinclude = require('gulp-file-include');

const paths = {
    scripts: {
        src: './',
        dest: './build/'
    }
};

async function includeHTML() {
    return gulp.src([
            '*.html',
            '!header.html',  
            '!footer.html'  
        ])
        .pipe(fileinclude({
            prefix: '@@',
            basepath: '@file'
        }))
        .pipe(gulp.dest(paths.scripts.dest));
}



exports.default = function() {
    gulp.src('./scss/**/*.scss')
        .pipe(gulp.dest('./css'))
        .on('end', done);
    done();

    return src('src/*.js')
        .pipe(babel())
        .pipe(src('vendor/*.js'))
        .pipe(dest('output/'))
        .pipe(uglify())
        .pipe(rename({ extname: '.min.js' }))
        .pipe(dest('output/'));

}


exports.default = includeHTML;