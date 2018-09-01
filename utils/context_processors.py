import datetime

import contacts.models
import utils


def current_date(context):
    return {
        'CURRENT_DATE': utils.today(),
        'ONE_WEEK': utils.today() + datetime.timedelta(weeks=1),
        'FOUR_WEEKS': utils.today() + datetime.timedelta(weeks=4)
    }


def brand_status(context):
    # Make this always return success for now. We will probably do this from angular later
    return {'BRAND_STATUS': "brand-status-success"}

    # do we have work to do?
    nonzero = 0
    visits = contacts.models.Visit.objects.for_user(context.user)
    if visits.get_bookcheck().count() + visits.get_upcoming_visits().count() > 0: nonzero = nonzero + 1
    if contacts.models.Message.objects.for_user(context.user).filter(is_viewed=False).count() > 0: nonzero = nonzero + 1
    if 0 > 0: nonzero = nonzero + 1
    if contacts.models.Message.objects.for_user(context.user).to_translate().count() > 0: nonzero = nonzero + 1

    if nonzero > 0:
        # if nonzero == 1:
        # 	return {'BRAND_STATUS': "brand-status-warning"}
        return {'BRAND_STATUS': "brand-status-danger"}
    return {'BRAND_STATUS': "brand-status-success"}
