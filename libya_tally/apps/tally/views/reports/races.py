from django.views.generic import TemplateView
from guardian.mixins import LoginRequiredMixin

from libya_tally.libs.views.exports import valid_ballots
from libya_tally.libs.permissions import groups
from libya_tally.libs.reports import progress as p
from libya_tally.libs.views import mixins


class RacesReportView(LoginRequiredMixin,
                      mixins.GroupRequiredMixin,
                      TemplateView):
    group_required = groups.SUPER_ADMINISTRATOR
    template_name = 'tally/reports/races.html'

    def get_per_ballot_progress(self):
        data = []

        for ballot in valid_ballots():
            archived = p.ArchivedProgressReport().for_ballot(ballot)
            sc = ballot.sub_constituency

            if sc:
                data.append({
                    'ballot': ballot.number,
                    'district': sc.code,
                    'race_type': ballot.race_type_name,
                    'expected': archived.denominator,
                    'complete': archived.number,
                    'percentage': archived.percentage,
                })

        return data

    def get(self, *args, **kwargs):
        per_ballot = self.get_per_ballot_progress()
        races = len(per_ballot)
        completed = sum([1 for x in per_ballot if isinstance(
            x['percentage'], float) and x['percentage'] >= 100])

        overview = {
            'races': races,
            'completed': completed,
            'percentage': round(completed / float(races) * 100, 2)
        }

        return self.render_to_response(
            self.get_context_data(
                overview=overview,
                per_ballot=per_ballot))
