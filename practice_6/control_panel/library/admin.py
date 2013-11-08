from django.contrib import admin
from library.models import Book
from library.models import Author
from library.models import Publisher
from library.models import BooksImage
from django.contrib.contenttypes import generic


class AuthorsAdmin(admin.ModelAdmin):
    list_display=['last_name', 'first_name', 'email', 'year']
    list_display_links=['last_name', 'first_name']
    ordering=['last_name', 'first_name']

    def year(request, self):
        if self.birthyear:
            return self.birthyear
        else:
            return 'the age is unknown'


class BooksImageInline(generic.GenericTabularInline):
    model = BooksImage


class BooksAdmin(admin.ModelAdmin):
    list_display=['title', 'publisher', 'publication_date', 'cnt']
    inlines = [
        BooksImageInline,
    ]
    list_display_links=['title']
    search_fields=['title']
    fieldsets= (
        (None, {
            'fields': ('title', 'publication_date')
        }),
        ('Output data', {
            'fields': ('publisher', )
        }),
    )

    def cnt(self, obj):
        cnt=0
        for image in BooksImage.objects.filter(book_id=obj.id):
            cnt=image.images_cnt()
        return cnt

    cnt.allow_tags = True


class PublishersAdmin(admin.ModelAdmin):
    list_display=['title', 'country', 'city', ]
    list_display_links=['title']
    ordering=['title']
    list_filter=['country', 'city', ]
    fieldsets= (
        (None, {
            'fields': ('title',)
        }),
        ('Contact information', {
            'fields': ('country', 'city', 'address', )
        }),
    )


class BooksImagesAdmin(admin.ModelAdmin):
    list_display=['book', 'small_cover', 'cover', 'images_cnt']


admin.site.register(Author, AuthorsAdmin)
admin.site.register(Book, BooksAdmin)
admin.site.register(Publisher, PublishersAdmin)
admin.site.register(BooksImage, BooksImagesAdmin)
