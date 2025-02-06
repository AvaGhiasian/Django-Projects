from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "relax-by-the-sea",
        "image": "sea.jpg",
        "author": "Ava",
        "date": date(2025, 10, 2),
        "title": "Relaxing By the Shore",
        "excerpt": "There's nothing like the feeling that you get when you relax by \
        the sea side! It is an absolute silence.",
        "content": """
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quis
            soluta harum libero iure fugit saepe consequatur, obcaecati nesciunt id culpa
            illum! Cum eius consectetur optio facere ex, ea ipsam.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quis
            soluta harum libero iure fugit saepe consequatur, obcaecati nesciunt id culpa
            illum! Cum eius consectetur optio facere ex, ea ipsam.

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus quis
            soluta harum libero iure fugit saepe consequatur, obcaecati nesciunt id culpa
            illum! Cum eius consectetur optio facere ex, ea ipsam.

        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Ava",
        "date": date(2025, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Ava",
        "date": date(2024, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def start_page(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_posts = sorted_post[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all_posts.html", {
        "all_posts": all_posts
    })


def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post_detail.html", {
        "post": identified_post
    })
