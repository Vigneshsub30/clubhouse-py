package main

import (
	"github.com/clubhouse-api/mcp-server/config"
	"github.com/clubhouse-api/mcp-server/models"
	tools_get_all_topics "github.com/clubhouse-api/mcp-server/tools/get_all_topics"
	tools_get_suggested_follows_all "github.com/clubhouse-api/mcp-server/tools/get_suggested_follows_all"
	tools_get_suggested_follows_similar "github.com/clubhouse-api/mcp-server/tools/get_suggested_follows_similar"
	tools_update_username "github.com/clubhouse-api/mcp-server/tools/update_username"
	tools_invite_from_waitlist "github.com/clubhouse-api/mcp-server/tools/invite_from_waitlist"
	tools_get_topic "github.com/clubhouse-api/mcp-server/tools/get_topic"
	tools_get_suggested_follows_friends_only "github.com/clubhouse-api/mcp-server/tools/get_suggested_follows_friends_only"
	tools_get_channels "github.com/clubhouse-api/mcp-server/tools/get_channels"
	tools_get_following "github.com/clubhouse-api/mcp-server/tools/get_following"
	tools_join_channel "github.com/clubhouse-api/mcp-server/tools/join_channel"
	tools_check_waitlist_status "github.com/clubhouse-api/mcp-server/tools/check_waitlist_status"
	tools_get_clubs_for_topic "github.com/clubhouse-api/mcp-server/tools/get_clubs_for_topic"
	tools_get_suggested_club_invites "github.com/clubhouse-api/mcp-server/tools/get_suggested_club_invites"
	tools_record_action_trails "github.com/clubhouse-api/mcp-server/tools/record_action_trails"
	tools_get_settings "github.com/clubhouse-api/mcp-server/tools/get_settings"
	tools_get_welcome_channel "github.com/clubhouse-api/mcp-server/tools/get_welcome_channel"
	tools_get_suggested_invites "github.com/clubhouse-api/mcp-server/tools/get_suggested_invites"
	tools_call_phone_number_auth "github.com/clubhouse-api/mcp-server/tools/call_phone_number_auth"
	tools_resend_phone_number_auth "github.com/clubhouse-api/mcp-server/tools/resend_phone_number_auth"
	tools_check_for_update "github.com/clubhouse-api/mcp-server/tools/check_for_update"
	tools_invite_to_app "github.com/clubhouse-api/mcp-server/tools/invite_to_app"
	tools_get_club "github.com/clubhouse-api/mcp-server/tools/get_club"
	tools_get_events "github.com/clubhouse-api/mcp-server/tools/get_events"
	tools_get_profile "github.com/clubhouse-api/mcp-server/tools/get_profile"
	tools_get_release_notes "github.com/clubhouse-api/mcp-server/tools/get_release_notes"
	tools_create_channel "github.com/clubhouse-api/mcp-server/tools/create_channel"
	tools_get_suggested_speakers "github.com/clubhouse-api/mcp-server/tools/get_suggested_speakers"
	tools_refresh_token "github.com/clubhouse-api/mcp-server/tools/refresh_token"
	tools_me "github.com/clubhouse-api/mcp-server/tools/me"
	tools_get_actionable_notifications "github.com/clubhouse-api/mcp-server/tools/get_actionable_notifications"
	tools_follow "github.com/clubhouse-api/mcp-server/tools/follow"
	tools_get_notifications "github.com/clubhouse-api/mcp-server/tools/get_notifications"
	tools_get_online_friends "github.com/clubhouse-api/mcp-server/tools/get_online_friends"
	tools_get_users_for_topic "github.com/clubhouse-api/mcp-server/tools/get_users_for_topic"
	tools_leave_channel "github.com/clubhouse-api/mcp-server/tools/leave_channel"
	tools_search_clubs "github.com/clubhouse-api/mcp-server/tools/search_clubs"
	tools_update_notifications "github.com/clubhouse-api/mcp-server/tools/update_notifications"
	tools_search_users "github.com/clubhouse-api/mcp-server/tools/search_users"
	tools_get_create_channel_targets "github.com/clubhouse-api/mcp-server/tools/get_create_channel_targets"
	tools_start_phone_number_auth "github.com/clubhouse-api/mcp-server/tools/start_phone_number_auth"
	tools_complete_phone_number_auth "github.com/clubhouse-api/mcp-server/tools/complete_phone_number_auth"
)

func GetAll(cfg *config.APIConfig) []models.Tool {
	return []models.Tool{
		tools_get_all_topics.CreateGet_get_all_topicsTool(cfg),
		tools_get_suggested_follows_all.CreateGet_get_suggested_follows_allTool(cfg),
		tools_get_suggested_follows_similar.CreatePost_get_suggested_follows_similarTool(cfg),
		tools_update_username.CreatePost_update_usernameTool(cfg),
		tools_invite_from_waitlist.CreatePost_invite_from_waitlistTool(cfg),
		tools_get_topic.CreatePost_get_topicTool(cfg),
		tools_get_suggested_follows_friends_only.CreatePost_get_suggested_follows_friends_onlyTool(cfg),
		tools_get_channels.CreateGet_get_channelsTool(cfg),
		tools_get_following.CreatePost_get_followingTool(cfg),
		tools_join_channel.CreatePost_join_channelTool(cfg),
		tools_check_waitlist_status.CreatePost_check_waitlist_statusTool(cfg),
		tools_get_clubs_for_topic.CreatePost_get_clubs_for_topicTool(cfg),
		tools_get_suggested_club_invites.CreatePost_get_suggested_club_invitesTool(cfg),
		tools_record_action_trails.CreatePost_record_action_trailsTool(cfg),
		tools_get_settings.CreateGet_get_settingsTool(cfg),
		tools_get_welcome_channel.CreateGet_get_welcome_channelTool(cfg),
		tools_get_suggested_invites.CreatePost_get_suggested_invitesTool(cfg),
		tools_call_phone_number_auth.CreatePost_call_phone_number_authTool(cfg),
		tools_resend_phone_number_auth.CreatePost_resend_phone_number_authTool(cfg),
		tools_check_for_update.CreateGet_check_for_updateTool(cfg),
		tools_invite_to_app.CreatePost_invite_to_appTool(cfg),
		tools_get_club.CreatePost_get_clubTool(cfg),
		tools_get_events.CreateGet_get_eventsTool(cfg),
		tools_get_profile.CreatePost_get_profileTool(cfg),
		tools_get_release_notes.CreatePost_get_release_notesTool(cfg),
		tools_create_channel.CreatePost_create_channelTool(cfg),
		tools_get_suggested_speakers.CreatePost_get_suggested_speakersTool(cfg),
		tools_refresh_token.CreatePost_refresh_tokenTool(cfg),
		tools_me.CreatePost_meTool(cfg),
		tools_get_actionable_notifications.CreateGet_get_actionable_notificationsTool(cfg),
		tools_follow.CreatePost_followTool(cfg),
		tools_get_notifications.CreateGet_get_notificationsTool(cfg),
		tools_get_online_friends.CreatePost_get_online_friendsTool(cfg),
		tools_get_users_for_topic.CreateGet_get_users_for_topicTool(cfg),
		tools_leave_channel.CreatePost_leave_channelTool(cfg),
		tools_search_clubs.CreatePost_search_clubsTool(cfg),
		tools_update_notifications.CreatePost_update_notificationsTool(cfg),
		tools_search_users.CreatePost_search_usersTool(cfg),
		tools_get_create_channel_targets.CreatePost_get_create_channel_targetsTool(cfg),
		tools_start_phone_number_auth.CreatePost_start_phone_number_authTool(cfg),
		tools_complete_phone_number_auth.CreatePost_complete_phone_number_authTool(cfg),
	}
}
