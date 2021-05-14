# imports

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time



#path to your workspace
set_workspace(path=None)




def job():
    #login credentials
    insta_username = 'electro.wifi'
    insta_password = 'sdq590*98'

    comments = ['Buen post! @{}',
            'Amo tu perfil! @{}',
            'Tu feed es una inspiracion :thumbsup:',
            'Simplemente increible:open_mouth:',
            'Que camaras usas? @{}?',
            'Amo tu post@{}',
            'Luce increible @{}',
            'Me siento inspirado por ti @{}',
            ':raised_hands: si!',
            'Puedo sentir tu pasion@{} :muscle:']

    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background


    session = InstaPy(username=insta_username, password=insta_password)


    
    session.set_quota_supervisor(enabled=True,
                                sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h", "server_calls_d"],
                                sleepyhead=True,
                                stochastic_flow=True,
                                notify_me=True,
                                peak_likes_hourly=57,
                                peak_likes_daily=585,
                                peak_comments_hourly=21,
                                peak_comments_daily=182,
                                peak_follows_hourly=5,
                                peak_follows_daily=25,
                                peak_unfollows_hourly=5,
                                peak_unfollows_daily=25,
                                peak_server_calls_hourly=None,
                                peak_server_calls_daily=2500)


    with smart_run(session):
        """ Activity flow """		
    # general settings		
    session.set_dont_include(["friend1", "friend2", "friend3"])		
    
    # activity		
    session.like_by_tags(["cecomsa"], amount=10)

    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.join_pods(topic='tecnologia', engagement_mode='no_comments')


job()

